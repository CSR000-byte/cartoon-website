/* ============================================
   🐱 卡创 · 星际小猫号 — 全局交互脚本
   Space Kitten Odyssey - Global Interactions
   ============================================ */

// ============================================
// ⭐ Canvas 动态星空背景
// ============================================
(function initStarCanvas() {
  const canvas = document.getElementById('stars-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let stars = [];
  let animationId;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  function createStars(count) {
    stars = [];
    for (let i = 0; i < count; i++) {
      stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 2.5 + 0.5,
        opacity: Math.random(),
        speed: Math.random() * 0.02 + 0.005,
        phase: Math.random() * Math.PI * 2,
        color: ['#ffffff', '#A29BFE', '#00CEC9', '#FDCB6E', '#FF7675'][Math.floor(Math.random() * 5)]
      });
    }
  }

  function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    stars.forEach(star => {
      star.opacity += star.speed;
      if (star.opacity > 1 || star.opacity < 0.15) {
        star.speed = -star.speed;
      }

      ctx.beginPath();
      ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
      ctx.fillStyle = star.color;
      ctx.globalAlpha = star.opacity;
      ctx.fill();

      // 发光效果
      if (star.radius > 1.5) {
        ctx.beginPath();
        ctx.arc(star.x, star.y, star.radius * 2.5, 0, Math.PI * 2);
        ctx.fillStyle = star.color;
        ctx.globalAlpha = star.opacity * 0.2;
        ctx.fill();
      }
    });

    ctx.globalAlpha = 1;
  }

  function animate() {
    drawStars();
    animationId = requestAnimationFrame(animate);
  }

  function handleResize() {
    resize();
    createStars(Math.floor((canvas.width * canvas.height) / 8000));
  }

  window.addEventListener('resize', handleResize);
  handleResize();
  animate();

  // 清理函数（SPA 场景）
  window._cleanupStars = () => {
    cancelAnimationFrame(animationId);
    window.removeEventListener('resize', handleResize);
  };
})();

// ============================================
// 🧭 移动端导航菜单
// ============================================
(function initMobileNav() {
  const toggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  if (!toggle || !navLinks) return;

  toggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    toggle.textContent = isOpen ? '✕' : '☰';
  });

  // 点击导航链接后关闭菜单
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      toggle.textContent = '☰';
    });
  });

  // 点击外部关闭菜单
  document.addEventListener('click', (e) => {
    if (!toggle.contains(e.target) && !navLinks.contains(e.target)) {
      navLinks.classList.remove('open');
      toggle.textContent = '☰';
    }
  });
})();

// ============================================
// ⬆️ 回到顶部按钮
// ============================================
(function initBackToTop() {
  const btn = document.getElementById('backToTop');
  if (!btn) return;

  function toggleVisibility() {
    if (window.scrollY > 400) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }

  window.addEventListener('scroll', toggleVisibility, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // 初始检查
  toggleVisibility();
})();

// ============================================
// 🍞 Toast 通知
// ============================================
function showToast(message, duration = 2500) {
  const toast = document.getElementById('toast');
  if (!toast) return;

  // 清除之前的定时器
  if (toast._timeout) {
    clearTimeout(toast._timeout);
    toast.classList.remove('show');
  }

  toast.textContent = message;
  // 强制回流
  void toast.offsetWidth;
  toast.classList.add('show');

  toast._timeout = setTimeout(() => {
    toast.classList.remove('show');
  }, duration);
}

// ============================================
// 🌐 API 基础配置
// ============================================
const API_BASE = window.location.origin;

async function apiFetch(path, options = {}) {
  const url = `${API_BASE}${path}`;
  const config = {
    headers: { 'Content-Type': 'application/json' },
    ...options
  };
  const res = await fetch(url, config);
  const data = await res.json();
  if (!res.ok) {
    throw new Error(data.error || `请求失败 (${res.status})`);
  }
  return data;
}

// ============================================
// 📧 联系表单处理
// ============================================
async function handleContactSubmit(event) {
  event.preventDefault();

  const form = event.target;
  const submitBtn = form.querySelector('button[type="submit"]');
  const name = form.querySelector('#name')?.value || '';
  const email = form.querySelector('#email')?.value || '';
  const subject = form.querySelector('#subject')?.value || '';
  const message = form.querySelector('#message')?.value || '';

  // 简单的表单验证
  if (!name.trim() || !email.trim() || !subject.trim() || !message.trim()) {
    showToast('⚠️ 请填写所有字段后再发送哦～');
    return;
  }

  if (!email.includes('@') || !email.includes('.')) {
    showToast('📧 请输入正确的邮箱地址～');
    return;
  }

  // 禁用按钮防止重复提交
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.textContent = '⏳ 发送中…';
  }

  try {
    const result = await apiFetch('/api/contact', {
      method: 'POST',
      body: JSON.stringify({ name, email, subject, message })
    });
    showToast(result.message || '🚀 星际信号已发送！谢谢你的留言～', 3500);
    form.reset();
  } catch (err) {
    showToast('⚠️ 发送失败，请稍后重试…（后台服务未启动？）', 3500);
    console.error('联系表单提交失败:', err);
  } finally {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.textContent = '🚀 发送星际信号';
    }
  }
}

// ============================================
// 🌓 暗色/亮色主题切换（可选功能）
// ============================================
(function initThemeToggle() {
  const toggle = document.getElementById('themeToggle');
  if (!toggle) return;

  // 恢复保存的主题
  const savedTheme = localStorage.getItem('cartoon-theme');
  if (savedTheme === 'light') {
    document.body.classList.add('light-theme');
    toggle.textContent = '☀️';
  }

  toggle.addEventListener('click', () => {
    const isLight = document.body.classList.toggle('light-theme');
    toggle.textContent = isLight ? '☀️' : '🌓';
    localStorage.setItem('cartoon-theme', isLight ? 'light' : 'dark');
    showToast(isLight ? '☀️ 已切换到亮色模式' : '🌙 已切换到暗色模式', 2000);
  });
})();

// ============================================
// 🎯 页面加载完成后的初始化
// ============================================
document.addEventListener('DOMContentLoaded', () => {
  console.log('🐱🚀 卡创 · 星际小猫号 — 准备发射！');
  console.log('✨ 所有系统正常运行，星际小猫号向你问好～');
  console.log('🌌 浏览愉快！记得看看我们的角色和故事哦～');
});

// ============================================
// 📊 滚动动画（Intersection Observer）
// ============================================
(function initScrollAnimations() {
  if (!('IntersectionObserver' in window)) return;

  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'slideUp 0.6s ease forwards';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // 观察所有卡片元素
  document.querySelectorAll('.card, .gallery-item, .team-card').forEach(el => {
    el.style.opacity = '0';
    observer.observe(el);
  });

  // 初始显示的卡片直接展示
  setTimeout(() => {
    document.querySelectorAll('.card, .gallery-item, .team-card').forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight) {
        el.style.animation = 'slideUp 0.6s ease forwards';
      }
    });
  }, 100);
})();

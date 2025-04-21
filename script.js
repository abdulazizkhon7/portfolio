
document.querySelectorAll('.project-link').forEach(link => {
  link.addEventListener('click', event => {
      if (link.getAttribute('href') === "#") {
          event.preventDefault(); // Faqat noto‘g‘ri havolalar uchun o‘chiradi
          alert('This project will open soon!');
      }
  });
});


// .stars konteynerni topamiz
const starsContainer = document.querySelector('.stars');

// .stars mavjudligini tekshiramiz
if (starsContainer) {
  for (let i = 0; i < 100; i++) {
    const star = document.createElement('div'); // Yangi yulduz yaratamiz
    star.style.left = Math.random() * 100 + 'vw'; // Gorizontal joylashuv
    star.style.top = Math.random() * 100 + 'vh'; // Vertikal joylashuv
    star.style.width = star.style.height = Math.random() * 3 + 'px'; // Hajmi
    star.style.animationDuration = Math.random() * 10 + 5 + 's'; // Harakat tezligi
    starsContainer.appendChild(star); // .stars konteynerga qo‘shamiz
  }
} else {
  console.error('.stars konteyneri HTMLda topilmadi!');
}

// Modalni boshqarish
document.querySelectorAll('.project-link').forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      const modalId = link.dataset.project;
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.style.display = 'flex';
      }
    });
  });
  
  document.querySelectorAll('.modal .close').forEach(closeBtn => {
    closeBtn.addEventListener('click', () => {
      closeBtn.closest('.modal').style.display = 'none';
    });
  });
  
  window.addEventListener('click', event => {
    if (event.target.classList.contains('modal')) {
      event.target.style.display = 'none';
    }
  });
  

  window.addEventListener("scroll", () => {
    const btn = document.getElementById("backToTop");
    if (window.scrollY > 300) {
      btn.style.display = "block";
    } else {
      btn.style.display = "none";
    }
  });
  
  document.getElementById("backToTop").addEventListener("click", function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
  

window.addEventListener("load", () => {
  setTimeout(() => {
      document.getElementById("loading-screen").classList.add("fade-out");
  }, 2000); // 2 Sekunddan keyin loading yo‘qoladi
});


 //"Passionate about coding, design,and innovation.",
const texts = [
"コーディングはアート。一緒に作品を作ろう！",
"アイデア＋コード＝無限の可能性。",
"プロジェクトは冒険。一緒に始めよう！",
"プログラミングは無限。自分の世界を作ろう！"
];

let index = 0;
let charIndex = 0;
const typingSpeed = 100; // Harflar orasidagi kechikish (ms)
const delayBetweenTexts = 1500; // Matnlar orasidagi kechikish (ms)
const dynamicText = document.getElementById('dynamic-text');

function typeText() {
  if (charIndex < texts[index].length) {
      dynamicText.textContent += texts[index][charIndex];
      charIndex++;
      setTimeout(typeText, typingSpeed);
  } else {
      setTimeout(() => {
          dynamicText.textContent = '';
          charIndex = 0;
          index = (index + 1) % texts.length;
          typeText();
      }, delayBetweenTexts);
  }
}

// Funksiyani ishga tushirish
typeText();



// Intersection Observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible'); // 'visible' klassini qo‘shadi
    }
  });
}, { threshold: 0.1 }); // Element 10% ko‘rinishda bo‘lsa, animatsiya boshlanadi

// About Section-ni kuzatish
const aboutSection = document.querySelector('.about-section');
observer.observe(aboutSection);

// Bo‘limlarni boshqarish
const buttons = document.querySelectorAll('.tab-button');
const sections = document.querySelectorAll('.about-section-content');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const target = button.getAttribute('data-target');

        sections.forEach(section => {
            section.classList.remove('active');
        });

        document.getElementById(target).classList.add('active');
    });
});

// Boshlang‘ich bo‘limni ko‘rsatish
document.getElementById('quick-bio').classList.add('active');

const projects = [
  {
      title: "クラス日誌",
      description: "教師と学生 のための デジタルクラス日誌システムです。",
      image: "projectimg.png", // O'z rasmingizni yuklang
      link: "https://edutrack-zcta.onrender.com"
  },
  {
      title: "日本語学校検索",
      description: " 日本語学校検索システムです。",
      image: "projecttimu.png",
      link: "https://magenta-ohkq.onrender.com"
  },

];

const projectContainer = document.getElementById('projects-container');
const modal = document.getElementById('project-modal');
const modalTitle = document.getElementById('modal-title');
const modalImage = document.getElementById('modal-image');
const modalDescription = document.getElementById('modal-description');
const modalLink = document.getElementById('modal-link');
const closeModal = document.querySelector('.close-modal');

projects.forEach(project => {
  const projectCard = document.createElement('div');
  projectCard.classList.add('project-card');

  projectCard.innerHTML = `
      <img src="${project.image}" alt="${project.title}">
      <h3>${project.title}</h3>
      <p>${project.description}</p>
      
  `;

  projectCard.addEventListener('click', () => {
      modalTitle.textContent = project.title;
      modalImage.src = project.image;
      modalDescription.textContent = project.description;
      modalLink.href = project.link;
      modal.style.display = "flex";
  });

  projectContainer.appendChild(projectCard);
});

closeModal.addEventListener('click', () => {
  modal.style.display = "none";
});

window.addEventListener('click', (event) => {
  if (event.target === modal) {
      modal.style.display = "none";
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const loadingScreen = document.getElementById("loading-screen");
  const portfolio = document.getElementById("portfolio");

  // Lottie animatsiya yuklash
  lottie.loadAnimation({
      container: document.getElementById('loading-animation'),
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: 'screen.json' // Lottie JSON animatsiya fayli
  });

  // Loading tugagandan keyin portfelni ko‘rsatish
  setTimeout(() => {
      loadingScreen.classList.add("fade-out");
      setTimeout(() => {
          loadingScreen.style.display = "none";
          portfolio.style.display = "block";
      }, 250);
  }, 500); // 4 sekund kutish
});


lottie.loadAnimation({
  container: document.getElementById('about-animation'), // Animatsiya joylashuvi
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: '4.json' // JSON fayl manzili
});

lottie.loadAnimation({
  container: document.getElementById('lottie-animation'), // Animatsiya joyi
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'home.json' // JSON fayl manzili
});

lottie.loadAnimation({
  container: document.getElementById('skills-animation'), // Animatsiya joylashuvi
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'skills.json' // JSON fayl manzili
});

const music = document.getElementById("background-music");
const musicButton = document.getElementById("music-toggle");

musicButton.addEventListener("click", () => {
    if (music.paused) {
        music.play();
        musicButton.textContent = "⏸"; // Pause icon
    } else {
        music.pause();
        musicButton.textContent = "▶"; // Play icon
    }
});

document.addEventListener("DOMContentLoaded", function () {
  const starContainer = document.getElementById("star-container");
  const rocket = document.getElementById("rocket");
  const portfolio = document.getElementById("portfolio");
  const rocketSection = document.getElementById("rocket-section");

  // Yulduzlarni yaratish
  for (let i = 0; i < 100; i++) {
      let star = document.createElement("div");
      star.classList.add("star");
      star.style.top = Math.random() * 100 + "vh";
      star.style.left = Math.random() * 100 + "vw";
      star.style.opacity = Math.random();
      star.style.width = Math.random() * 3 + "px";
      star.style.height = star.style.width;
      starContainer.appendChild(star);
  }

  // Raketa uchishi
  setTimeout(() => {
      rocket.style.animation = "launch 5s ease-in-out forwards";
  }, 1000);

  // Portfelni ochish
  setTimeout(() => {
      rocketSection.classList.add("fade-out");
      setTimeout(() => {
          rocketSection.style.display = "none";
          portfolio.style.display = "block";
          portfolio.classList.add("fadeIn");
      }, 3000);
  }, 6000);
});

document.addEventListener("DOMContentLoaded", function () {
  const aboutAnimation = document.querySelector('.about-animation-container');
  const aboutForm = document.querySelector('.about-form');

  const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              aboutAnimation.classList.add('slide-in-left');
              aboutForm.classList.add('slide-in-right');
          } else {
              aboutAnimation.classList.remove('slide-in-left');
              aboutForm.classList.remove('slide-in-right');
          }
      });
  }, { threshold: 0.2 });

  observer.observe(aboutAnimation);
  observer.observe(aboutForm);
});

document.addEventListener("DOMContentLoaded", function () {
  const skillsAnimation = document.querySelector('.skills-animation');
  const skillsForm = document.querySelector('.skills-logos');

  const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              skillsAnimation.classList.add('slide-in-left');
              skillsForm.classList.add('slide-in-right');
          } else {
              skillsAnimation.classList.remove('slide-in-left');
              skillsForm.classList.remove('slide-in-right');
          }
      });
  }, { threshold: 0.2 });

  observer.observe(skillsAnimation);
  observer.observe(skillsForm);
});

document.addEventListener("DOMContentLoaded", function () {
  const projectCards = document.querySelectorAll(".project-card");

  const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              entry.target.classList.add('slide-in');
          } else {
              entry.target.classList.remove('slide-in'); // Qayta animatsiya qilish uchun
          }
      });
  }, { threshold: 0.3 });

  projectCards.forEach(card => {
      observer.observe(card);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const contactTitle = document.querySelector('.contact-title');
  const contactForm = document.querySelector('#contact-form');
  const contactDetails = document.querySelector('.contact-details');

  const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              contactTitle.classList.add('fade-in');
              contactForm.classList.add('slide-in-left');
              contactDetails.classList.add('slide-in-right');
          } else {
              contactTitle.classList.remove('fade-in');
              contactForm.classList.remove('slide-in-left');
              contactDetails.classList.remove('slide-in-right');
          }
      });
  }, { threshold: 0.3 });

  observer.observe(contactTitle);
  observer.observe(contactForm);
  observer.observe(contactDetails);
});           



document.addEventListener("DOMContentLoaded", function () {
  const homeLeft = document.querySelector('.home-left');
  const lottieAnimation = document.querySelector('.lottie-animation');

  const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              homeLeft.classList.add('slide-in-left');
              lottieAnimation.classList.add('slide-in-right');
          } else {
              homeLeft.classList.remove('slide-in-left');
              lottieAnimation.classList.remove('slide-in-right');
          }
      });
  }, { threshold: 0.3 });

  observer.observe(homeLeft);
  observer.observe(lottieAnimation);
});

document.addEventListener("DOMContentLoaded", function () {
  const skillsSection = document.querySelector("#skills");
  const progressBars = document.querySelectorAll(".progress-bar");

  function resetProgress() {
      progressBars.forEach((bar) => {
          bar.style.width = "0%"; // Skillsdan chiqganda 0% ga qaytarish
      });
  }

  const observer = new IntersectionObserver(
      (entries) => {
          entries.forEach((entry) => {
              if (entry.isIntersecting) {
                  console.log("Skills bo‘limi ekranga kirdi!"); // Konsolda tekshiramiz
                  progressBars.forEach((bar) => {
                      const targetWidth = bar.getAttribute("data-width"); // Asl foizni olish
                      bar.style.width = "0%"; // Dastlab 0%
                      setTimeout(() => {
                          bar.style.width = targetWidth; // Keyin asl foizga boradi
                      }, 500);
                  });
              } else {
                  console.log("Skills bo‘limidan chiqildi, progress resetlandi!"); // Konsol tekshiruvi
                  resetProgress(); // Skillsdan chiqsa progressni 0% qiladi
              }
          });
      },
      { threshold: 0.3 } // 30% bo‘lim ko‘ringanda ishga tushadi
  );

  observer.observe(skillsSection);
});

const menuBtn = document.querySelector('.menu-btn');
const navMenu = document.querySelector('.navbar ul');

menuBtn.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    
    // har safar bosilganda animatsiya yangilanishi uchun:
    document.querySelectorAll('.menu-item').forEach(item => {
        item.style.animation = 'none';
        setTimeout(() => {
            item.style.animation = '';
        }, 10);
    });
});

document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
    });
});


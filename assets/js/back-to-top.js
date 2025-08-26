// Back to Top Button Functionality
document.addEventListener('DOMContentLoaded', function() {
  // Create the back to top button
  const backToTopButton = document.createElement('button');
  backToTopButton.className = 'back-to-top';
  backToTopButton.setAttribute('aria-label', 'Back to top');
  backToTopButton.innerHTML = `
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path d="M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z"/>
    </svg>
  `;
  
  // Add the button to the page
  document.body.appendChild(backToTopButton);
  
  // Show/hide button based on scroll position
  function toggleBackToTop() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const windowHeight = window.innerHeight;
    
    // Show button when scrolled down more than one viewport height
    if (scrollTop > windowHeight) {
      backToTopButton.classList.add('show');
    } else {
      backToTopButton.classList.remove('show');
    }
  }
  
  // Smooth scroll to top when button is clicked
  backToTopButton.addEventListener('click', function(e) {
    e.preventDefault();
    
    // Smooth scroll to top
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
    
    // Focus on the main content for accessibility
    const mainContent = document.querySelector('main') || document.querySelector('.main-content');
    if (mainContent) {
      mainContent.focus();
    }
  });
  
  // Listen for scroll events
  window.addEventListener('scroll', toggleBackToTop);
  
  // Initial check
  toggleBackToTop();
});

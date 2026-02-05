// SEO and Conversion Optimization Script
// Add this script before the closing </body> tag in index.html

// ============================================================================
// ANALYTICS TRACKING
// ============================================================================

// Google Analytics 4 - Replace 'G-XXXXXXXXXX' with your actual GA4 measurement ID
// Uncomment and configure when ready
/*
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-XXXXXXXXXX');
*/

// Facebook Pixel - Replace 'XXXXXXXXXX' with your actual Pixel ID
// Uncomment and configure when ready
/*
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'XXXXXXXXXX');
fbq('track', 'PageView');
*/

// ============================================================================
// FORM SUBMISSION HANDLER
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#contact form');
    if (!form) return;
    
    const submitButton = form.querySelector('button[type="button"]');
    if (submitButton) {
        submitButton.setAttribute('type', 'submit');
    }
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get form data
        const name = form.querySelector('input[name="name"]').value;
        const email = form.querySelector('input[name="email"]').value;
        const phone = form.querySelector('input[name="phone"]').value;
        const message = form.querySelector('textarea[name="message"]').value;
        
        // Basic validation
        if (!name || !email || !phone) {
            alert('Please fill in all required fields (Name, Email, and Phone).');
            return;
        }
        
        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address.');
            return;
        }
        
        // Phone validation
        const phoneRegex = /^[\d\s\+\-\(\)]+$/;
        if (!phoneRegex.test(phone)) {
            alert('Please enter a valid phone number.');
            return;
        }
        
        // Disable submit button
        submitButton.disabled = true;
        submitButton.innerHTML = '<span>Sending...</span>';
        
        // Track conversion event
        if (typeof gtag !== 'undefined') {
            gtag('event', 'generate_lead', {
                'event_category': 'Form',
                'event_label': 'Office Space Inquiry'
            });
        }
        
        if (typeof fbq !== 'undefined') {
            fbq('track', 'Lead');
        }
        
        // Prepare data
        const data = {
            name: name,
            email: email,
            phone: phone,
            message: message,
            property: 'Downtown Tech Park Office Space',
            timestamp: new Date().toISOString(),
            source: window.location.href
        };
        
        // Form submission
        // OPTION 1: Using FormSubmit.co (free service)
        // 1. Replace 'your-email@example.com' with your actual email
        // 2. Submit form once to verify your email
        try {
            const response = await fetch('https://formsubmit.co/ajax/your-email@example.com', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                // Success message
                form.innerHTML = `
                    <div class="text-center py-8">
                        <div class="w-16 h-16 bg-green-100 dark:bg-green-900/30 rounded-full flex items-center justify-center mx-auto mb-4">
                            <span class="material-symbols-outlined text-green-600 text-3xl">check_circle</span>
                        </div>
                        <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">Thank You!</h3>
                        <p class="text-slate-600 dark:text-slate-400">We've received your inquiry and will contact you within 24 hours.</p>
                        <p class="text-sm text-slate-500 mt-4">Check your email for confirmation.</p>
                    </div>
                `;
            } else {
                throw new Error('Form submission failed');
            }
        } catch (error) {
            console.error('Form submission error:', error);
            alert('There was an error submitting the form. Please try calling us directly or sending a WhatsApp message.');
            submitButton.disabled = false;
            submitButton.innerHTML = '<span>Send Inquiry</span><span class="material-symbols-outlined text-sm">send</span>';
        }
    });
});

// ============================================================================
// LAZY LOADING FOR IMAGES (if browser doesn't support native lazy loading)
// ============================================================================

if ('loading' in HTMLImageElement.prototype) {
    // Browser supports native lazy loading
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        img.src = img.src;
    });
} else {
    // Fallback for browsers that don't support lazy loading
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
    document.body.appendChild(script);
}

// ============================================================================
// TRACK PHONE CLICKS
// ============================================================================

document.querySelectorAll('a[href^="tel:"]').forEach(link => {
    link.addEventListener('click', function() {
        if (typeof gtag !== 'undefined') {
            gtag('event', 'phone_click', {
                'event_category': 'Contact',
                'event_label': 'Phone Number Click'
            });
        }
        
        if (typeof fbq !== 'undefined') {
            fbq('trackCustom', 'PhoneClick');
        }
    });
});

// ============================================================================
// TRACK WHATSAPP CLICKS
// ============================================================================

document.querySelectorAll('a[href^="https://wa.me"]').forEach(link => {
    link.addEventListener('click', function() {
        if (typeof gtag !== 'undefined') {
            gtag('event', 'whatsapp_click', {
                'event_category': 'Contact',
                'event_label': 'WhatsApp Click'
            });
        }
        
        if (typeof fbq !== 'undefined') {
            fbq('trackCustom', 'WhatsAppClick');
        }
    });
});

// ============================================================================
// SCROLL DEPTH TRACKING
// ============================================================================

let scrollDepths = [25, 50, 75, 100];
let scrollTracked = [];

window.addEventListener('scroll', function() {
    const scrollPercent = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight * 100;
    
    scrollDepths.forEach(depth => {
        if (scrollPercent >= depth && !scrollTracked.includes(depth)) {
            scrollTracked.push(depth);
            
            if (typeof gtag !== 'undefined') {
                gtag('event', 'scroll_depth', {
                    'event_category': 'Engagement',
                    'event_label': depth + '%',
                    'value': depth
                });
            }
        }
    });
});

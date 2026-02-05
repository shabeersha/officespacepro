// SEO and Conversion Optimization Script
// Production-ready version

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
// TRACK PHONE CLICKS
// ============================================================================

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('a[href^="tel:"]').forEach(function (link) {
        link.addEventListener('click', function () {
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

    document.querySelectorAll('a[href^="https://wa.me"]').forEach(function (link) {
        link.addEventListener('click', function () {
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
});

// ============================================================================
// SCROLL DEPTH TRACKING
// ============================================================================

var scrollDepths = [25, 50, 75, 100];
var scrollTracked = [];

window.addEventListener('scroll', function () {
    var scrollPercent = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight * 100;

    scrollDepths.forEach(function (depth) {
        if (scrollPercent >= depth && scrollTracked.indexOf(depth) === -1) {
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

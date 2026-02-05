// Form submission handler for Google Sheets integration
// Compatible with all browsers including older mobile browsers
document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('inquiryForm');

    if (!form) {
        console.error('Form with id "inquiryForm" not found');
        return;
    }

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Get form data
        var nameInput = document.querySelector('input[name="name"]');
        var phoneInput = document.querySelector('input[name="phone"]');
        var sourceInput = document.querySelector('input[name="source"]');

        var formData = {
            name: nameInput ? nameInput.value : '',
            phone: phoneInput ? phoneInput.value : '',
            source: sourceInput ? sourceInput.value : 'website',
            timestamp: new Date().toISOString()
        };

        // Google Apps Script Web App URL
        var scriptURL = 'https://script.google.com/macros/s/AKfycbzLpwYQPztgmSEegdHWy40fQSxzLuPYZVGwzYioEkta-Tc1f8j8yYKnJfasItz1-qBw/exec';

        try {
            // Get submit button
            var submitBtn = form.querySelector('button[type="submit"]');
            var originalHTML = submitBtn.innerHTML;

            // Show loading state
            submitBtn.innerHTML = '<span class="material-symbols-outlined animate-spin">progress_activity</span> Sending...';
            submitBtn.disabled = true;

            // Send to Google Sheets (fire and forget - no-cors mode doesn't allow reading response anyway)
            // Use XMLHttpRequest for better compatibility if fetch is not available
            if (window.fetch) {
                fetch(scriptURL, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                }).catch(function (error) {
                    console.error('Error:', error);
                });
            } else {
                // Fallback for older browsers
                var xhr = new XMLHttpRequest();
                xhr.open('POST', scriptURL, true);
                xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.send(JSON.stringify(formData));
            }

            // Show success immediately (don't wait for response)
            setTimeout(function () {
                // Show success message
                submitBtn.innerHTML = '<span class="material-symbols-outlined">check_circle</span> Sent Successfully!';
                submitBtn.classList.remove('bg-primary', 'hover:bg-blue-600');
                submitBtn.classList.add('bg-green-600');

                // Reset form
                form.reset();

                // Show custom thank you modal
                var thankYouModal = document.getElementById('thankYouModal');
                if (thankYouModal) {
                    thankYouModal.classList.remove('hidden');
                    thankYouModal.classList.add('flex');
                    document.body.style.overflow = 'hidden';
                }

                // Restore button after 3 seconds
                setTimeout(function () {
                    submitBtn.innerHTML = originalHTML;
                    submitBtn.disabled = false;
                    submitBtn.classList.remove('bg-green-600');
                    submitBtn.classList.add('bg-primary', 'hover:bg-blue-600');
                }, 3000);
            }, 500); // Small delay for better UX

        } catch (error) {
            console.error('Error:', error);

            // Show error state
            var submitBtn = form.querySelector('button[type="submit"]');
            submitBtn.innerHTML = '<span class="material-symbols-outlined">error</span> Error - Try Again';
            submitBtn.classList.remove('bg-primary');
            submitBtn.classList.add('bg-red-600');

            alert('Something went wrong. Please try again or call us directly at +916282573625');

            // Restore button after 3 seconds
            setTimeout(function () {
                submitBtn.innerHTML = 'Schedule Personal Tour <span class="material-symbols-outlined">calendar_today</span>';
                submitBtn.disabled = false;
                submitBtn.classList.remove('bg-red-600');
                submitBtn.classList.add('bg-primary', 'hover:bg-blue-600');
            }, 3000);
        }
    });

    // Close thank you modal handler
    var closeThankYouBtn = document.getElementById('closeThankYouModal');
    if (closeThankYouBtn) {
        closeThankYouBtn.addEventListener('click', function () {
            var thankYouModal = document.getElementById('thankYouModal');
            if (thankYouModal) {
                thankYouModal.classList.remove('flex');
                thankYouModal.classList.add('hidden');
                document.body.style.overflow = '';
            }
        });
    }
});

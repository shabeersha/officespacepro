#!/bin/bash

# Script to add remaining SEO and conversion optimizations to index.html
# This adds Schema.org data, form handler, and analytics tracking

FILE="/Users/shabeerali/OfficeSpaceSalesPage/index.html"

# 1. Add Schema.org structured data before </head>
sed -i.bak '/<\/head>/i\
\
    <!-- Schema.org Structured Data for SEO -->\
    <script type="application/ld+json">\
    {\
      "@context": "https://schema.org",\
      "@type": "RealEstateListing",\
      "name": "Furnished Office Space for Sale - Downtown Tech Park",\
      "description": "A ready-to-move 1,200 sq. ft. workspace ideal for startups. Fully furnished, plug-and-play, and situated in the citys most prestigious business district.",\
      "url": "https://yourdomain.com/",\
      "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuD-ilv7zpZ_VG_zm1j0mqupTMPzzEPg8eFPrEe5qorR8yAd1-gfLRPuPuKQsUOHwlj02cKjAz0SDqksHfzh2s_jNEThjkU18VHG-pF487O1sINhjGtu_rD-_PvL1Aimn0plw7IuPZeeMAEDN907ngS6GitZYxSzJ-sTv_PdDsaBll1sv_gf_LdWrB3aC1ZazVNzwGqfojR7jGCUHw6Q94tNERfLdFhFA5Cm1M2iY0Q40sqDp_3eWNW2FOYrZnigstydxjU6Yomad8BO",\
      "address": {\
        "@type": "PostalAddress",\
        "streetAddress": "123 Innovation Blvd, Suite 400",\
        "addressLocality": "Tech City",\
        "addressRegion": "TC",\
        "postalCode": "90210",\
        "addressCountry": "US"\
      },\
      "offers": {\
        "@type": "Offer",\
        "price": "450000",\
        "priceCurrency": "USD",\
        "availability": "https://schema.org/InStock"\
      },\
      "floorSize": {\
        "@type": "QuantitativeValue",\
        "value": "1200",\
        "unitCode": "FTK"\
      }\
    }\
    </script>\
' "$FILE"

echo "✅ Schema.org structured data added"
echo "✅ Backup created at index.html.bak"
echo ""
echo "Next steps:"
echo "1. Replace WhatsApp button with link (manual edit needed)"
echo "2. Add form submission handler (JavaScript)"
echo "3. Add name attributes to form inputs"
echo "4. Configure analytics tracking IDs"

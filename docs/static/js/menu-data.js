/**
 * menu-data.js
 * ============
 * This file replaces the Django database-driven menu rendering.
 * To update the menu, edit the `menuData` array below.
 *
 * Each category has:
 *   - name: displayed as the tab label
 *   - items: array of menu items, each with:
 *       - name: dish name
 *       - description: short description
 *       - image: path to image (relative to docs/ root, e.g. "static/img/menu/dish.jpg")
 *
 * Gallery images are also defined here in `galleryImages`.
 */

const menuData = [
    {
        name: "Starters",
        items: [
            {
                name: "Chicken Tikka",
                description: "Tender chicken marinated in spiced yoghurt, grilled in a tandoor oven.",
                image: "static/img/menu/menu-01.jpg"
            },
            {
                name: "Vegetable Samosa",
                description: "Crispy pastry filled with spiced potatoes and peas, served with mint chutney.",
                image: "static/img/menu/menu-02.jpg"
            },
            {
                name: "Seekh Kebab",
                description: "Minced lamb blended with herbs and spices, skewered and chargrilled.",
                image: "static/img/menu/menu-03.jpg"
            },
            {
                name: "Onion Bhaji",
                description: "Golden fried onion fritters seasoned with cumin and fresh coriander.",
                image: "static/img/menu/menu-04.jpg"
            }
        ]
    },
    {
        name: "Main Course",
        items: [
            {
                name: "Lamb Rogan Josh",
                description: "Slow-cooked tender lamb in a rich, aromatic Kashmiri sauce.",
                image: "static/img/menu/menu-06.jpg"
            },
            {
                name: "Chicken Biryani",
                description: "Fragrant basmati rice layered with spiced chicken and caramelised onions.",
                image: "static/img/menu/menu-07.jpg"
            },
            {
                name: "Prawn Masala",
                description: "Juicy king prawns cooked in a tangy tomato and onion masala sauce.",
                image: "static/img/menu/menu-08.jpg"
            },
            {
                name: "Paneer Butter Masala",
                description: "Soft cottage cheese cubes in a creamy, mildly spiced tomato sauce.",
                image: "static/img/menu/menu-01.jpg"
            }
        ]
    },
    {
        name: "Desserts",
        items: [
            {
                name: "Gulab Jamun",
                description: "Soft milk-solid dumplings soaked in rose-flavoured sugar syrup.",
                image: "static/img/menu/menu-02.jpg"
            },
            {
                name: "Mango Kulfi",
                description: "Traditional Indian ice cream made with condensed milk and fresh mango.",
                image: "static/img/menu/menu-03.jpg"
            }
        ]
    },
    {
        name: "Drinks",
        items: [
            {
                name: "Mango Lassi",
                description: "Chilled yoghurt drink blended with sweet Alphonso mango.",
                image: "static/img/menu/menu-04.jpg"
            },
            {
                name: "Masala Chai",
                description: "Spiced milk tea brewed with cardamom, ginger, and cinnamon.",
                image: "static/img/menu/menu-06.jpg"
            }
        ]
    }
];

/**
 * Social gallery images shown in the footer.
 * Add image paths relative to docs/ root.
 */
const galleryImages = [
    "static/img/menu/menu-01.jpg",
    "static/img/menu/menu-02.jpg",
    "static/img/menu/menu-03.jpg",
    "static/img/menu/menu-04.jpg",
    "static/img/menu/menu-06.jpg",
    "static/img/menu/menu-07.jpg"
];

/* ---------------------------------------------------------------
   Rendering – no need to edit below this line
--------------------------------------------------------------- */

(function () {
    "use strict";

    function buildMenu() {
        const tabsEl = document.getElementById("menu-tabs");
        const contentEl = document.getElementById("menu-tab-content");

        if (!tabsEl || !contentEl) return;

        menuData.forEach(function (category, index) {
            const isFirst = index === 0;
            const tabId = "tab-" + (index + 1);

            // Build tab pill
            const li = document.createElement("li");
            li.className = "nav-item p-2";
            li.innerHTML =
                '<a class="d-flex py-2 mx-2 border border-primary bg-white rounded-pill' +
                (isFirst ? " active" : "") +
                '" data-bs-toggle="pill" href="#' + tabId + '">' +
                '<span class="text-dark" style="width:150px;">' + category.name + "</span>" +
                "</a>";
            tabsEl.appendChild(li);

            // Build tab pane
            const pane = document.createElement("div");
            pane.id = tabId;
            pane.className = "tab-pane fade show p-0" + (isFirst ? " active" : "");

            const row = document.createElement("div");
            row.className = "row g-4";

            category.items.forEach(function (item, itemIndex) {
                const col = document.createElement("div");
                col.className = "col-lg-6 wow bounceInUp";
                col.setAttribute("data-wow-delay", "0." + (itemIndex + 1) + "s");
                col.innerHTML =
                    '<div class="menu-item d-flex align-items-center">' +
                    '<img class="flex-shrink-0 img-fluid rounded-circle" src="' + item.image + '" alt="' + item.name + '">' +
                    '<div class="w-100 d-flex flex-column text-start ps-4">' +
                    '<div class="d-flex justify-content-between border-bottom border-primary pb-2 mb-2">' +
                    "<h4>" + item.name + "</h4>" +
                    "</div>" +
                    '<p class="mb-0">' + item.description + "</p>" +
                    "</div>" +
                    "</div>";
                row.appendChild(col);
            });

            pane.appendChild(row);
            contentEl.appendChild(pane);
        });
    }

    function buildGallery() {
        const galleryEl = document.getElementById("gallery-footer");
        if (!galleryEl) return;

        galleryImages.forEach(function (src) {
            const col = document.createElement("div");
            col.className = "col-4";
            col.innerHTML =
                '<img src="' + src + '" class="img-fluid rounded-circle border border-primary p-2" alt="Gallery image">';
            galleryEl.appendChild(col);
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        buildMenu();
        buildGallery();
    });
})();

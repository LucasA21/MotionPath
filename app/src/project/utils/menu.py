
def sidebar(request):
    menu = {
        "logo": {
            "url": "index.html",
            "src": "assets/compiled/svg/logo.svg",
            "alt": "Logo"
        },
        "menu_items": [
            {
                "title": "Inicio",
                "url": "dashboard",
                "icon": "house-fill",
            },
            {
                'for_admin': True,
                "separator": True,
                "title": "Usuario"
            },
            {
                'for_admin': True,
                "title": "Usuario",
                "url": "user_list",
                "icon": "person-fill",
            },
            #! =================================================================
            {
                "separator": True,
                "title": "Rutinas"
            },
            {
                'for_admin': True,
                "title": "Tipos de rutinas",
                "url": "rutine_type_list",
                "icon": "gear-fill",
            },
            {
                "title": "Crear Rutina",
                "url": "rutine_create",
                "icon": "plus-lg",
            },
            {
                "title": "Ver todas las rutinas",
                "url": "rutine_list",
                "icon": "card-list",
            },
            {
                "title": "Ver rutinas propias",
                "url": "own_rutine_list",
                "icon": "list-stars",
            },
            {
                "title": "Ver rutinas elegidas",
                "url": "picked_rutine_list",
                "icon": "card-checklist",
            },
            {
                "title": "Elegir una rutina",
                "url": "rutine_pick_one",
                "icon": "bookmark-check-fill",
            },
            #! =================================================================
            {
                "separator": True,
                "title": "Entrenadores"
            },
            {
                'for_trainer': True,
                "title": "Asignación de rutinas",
                "url": "assign_rutine_list",
                "icon": "calendar-check-fill",
            },
            {
                "title": "Ver entrenadores",
                "url": "trainer_list",
                "icon": "person-video2",
            },
            {
                "title": "Convertirse en entrenador",
                "url": "trainer_make",
                "icon": "person-arms-up",
            },
            #! =================================================================
            {
                "separator": True,
                "title": "Progreso"
            },
            {
                "title": "Progreso",
                "url": "progress_list",
                "icon": "graph-up-arrow",
            },
            {
                "separator": True,
                "title": "Ejercicio"
            },
            {
                "title": "Ejercicio",
                "url": "exercise_list",
                "icon": "person-walking",
            },
            {
                'for_admin': True,
                "title": "Tipo de ejercicios",
                "url": "exercise_type_list",
                "icon": "bar-chart-steps",
            },
            {
                'for_admin': True,
                "title": "Músculos",
                "url": "muscle_exercise_list",
                "icon": "person-arms-up",
            },
            {
                'for_admin': True,
                "title": "Nivel de dificultad",
                "url": "difficulty_level_list",
                "icon": "sort-numeric-up-alt",
            }


        ],
    }    
    return {'sidebar_menu': menu}



# menu_ejemplo = {
#     "logo": {
#         "url": "index.html",
#         "src": "assets/compiled/svg/logo.svg",
#         "alt": "Logo"
#     },
#     "menu_items": [
#         {
#             "separator": True,
#             "title": "Menu"
#         },
#         {
#             "title": "Dashboard",
#             "url": "index.html",
#             "icon": "grid-fill",
#             # "active": True
#         },
#         {
#             "title": "Components",
#             "icon": "stack",
#             "sub_items": [
#                 {
#                     "title": "Accordion", 
#                     "url": "component-accordion.html"
#                 },
#                 {
#                     "title": "Alert", 
#                     "url": "component-alert.html"
#                 },
#                 {
#                     "title": "Badge", 
#                     "url": "component-badge.html"
#                 },
#                 {
#                     "title": "Breadcrumb", 
#                     "url": "component-breadcrumb.html"
#                 },
#                 {
#                     "title": "Buttons", 
#                     "url": "component-buttons.html"
#                 },
#                 {
#                     "title": "Card", 
#                     "url": "component-card.html"
#                 },
#                 {
#                     "title": "Carousel", 
#                     "url": "component-carousel.html"
#                 },
#                 {
#                     "title": "Collapse", 
#                     "url": "component-collapse.html"
#                 },
#                 {
#                     "title": "Dropdowns", 
#                     "url": "component-dropdowns.html"
#                 },
#                 {
#                     "title": "List Group", 
#                     "url": "component-list-group.html"
#                 },
#                 {
#                     "title": "Modal", 
#                     "url": "component-modal.html"
#                 },
#                 {
#                     "title": "Navs", 
#                     "url": "component-navs.html"
#                 },
#                 {
#                     "title": "Pagination", 
#                     "url": "component-pagination.html"
#                 },
#                 {
#                     "title": "Popovers", 
#                     "url": "component-popovers.html"
#                 },
#                 {
#                     "title": "Progress", 
#                     "url": "component-progress.html"
#                 },
#                 {
#                     "title": "Spinners", 
#                     "url": "component-spinners.html"
#                 },
#                 {
#                     "title": "Tabs", 
#                     "url": "component-tabs.html"
#                 },
#                 {
#                     "title": "Tooltips", 
#                     "url": "component-tooltips.html"
#                 }
#             ]
#         },
#         {
#             "title": "Extra Components",
#             "icon": "collection-fill",
#             "sub_items": [
#                 {
#                     "title": "Avatar", 
#                     "url": "extra-component-avatar.html"
#                 },
#                 {
#                     "title": "Divider", 
#                     "url": "extra-component-divider.html"
#                 },
#                 {
#                     "title": "Date Picker", 
#                     "url": "extra-component-date-picker.html"
#                 },
#                 {
#                     "title": "Sweet Alert", 
#                     "url": "extra-component-sweetalert.html"
#                 },
#                 {
#                     "title": "Toastify", 
#                     "url": "extra-component-toastify.html"
#                 },
#                 {
#                     "title": "Rating", 
#                     "url": "extra-component-rating.html"
#                 },
#             ]
#         },
#         {
#             "title": "Layouts",
#             "icon": "grid-1x2-fill",
#             "sub_items": [
#                 {
#                     "title": "Default Layout", 
#                     "url": "layout-default.html"
#                 },
#                 {
#                     "title": "1 Column", 
#                     "url": "layout-vertical-1-column.html"
#                 },
#                 {
#                     "title": "Vertical Navbar", 
#                     "url": "layout-vertical-navbar.html"
#                 },
#                 {
#                     "title": "RTL Layout", 
#                     "url": "layout-rtl.html"
#                 },
#                 {
#                     "title": "Horizontal Menu", 
#                     "url": "layout-horizontal.html"
#                 },
#             ]
#         },
#         {
#             "separator": True,
#             "title": "Forms & Tables"
#         },
#         {
#             "title": "Form Elements",
#             "icon": "hexagon-fill",
#             "sub_items": [
#                 {
#                     "title": "Input", 
#                     "url": "form-element-input.html"
#                 },
#                 {
#                     "title": "Input Group", 
#                     "url": "form-element-input-group.html"
#                 },
#                 {
#                     "title": "Select", 
#                     "url": "form-element-select.html"
#                 },
#                 {
#                     "title": "Radio", 
#                     "url": "form-element-radio.html"
#                 },
#                 {
#                     "title": "Checkbox", 
#                     "url": "form-element-checkbox.html"
#                 },
#                 {
#                     "title": "Textarea", 
#                     "url": "form-element-textarea.html"
#                 },
#             ]
#         },
#         {
#             "title": "Form Layouts",
#             "url": "form-layouts.html",
#             "icon": "file-earmark-medical-fill",
#         },
#         {
#             "title": "Form Validation",
#             "icon": "journal-check",
#             "sub_items": [
#                 {
#                     "title": "Parsley", 
#                     "url": "form-validation-parsley.html"
#                 },
#             ]
#         },
#         {
#             "title": "Form Editor",
#             "icon": "pen-fill",
#             "sub_items": [
#                 {
#                     "title": "Quill", 
#                     "url": "form-editor-quill.html"
#                 },
#                 {
#                     "title": "CKEditor", 
#                     "url": "form-editor-ckeditor.html"
#                 },
#                 {
#                     "title": "Summernote", 
#                     "url": "form-editor-summernote.html"
#                 },
#                 {
#                     "title": "TinyMCE", 
#                     "url": "form-editor-tinymce.html"
#                 },
#             ]
#         },
#         {
#             "title": "Table",
#             "url": "table.html",
#             "icon": "grid-1x2-fill",
#         },
#         {
#             "title": "Datatables",
#             "icon": "file-earmark-spreadsheet-fill",
#             "sub_items": [
#                 {
#                     "title": "Datatable", 
#                     "url": "table-datatable.html"
#                 },
#                 {
#                     "title": "Datatable (jQuery)", 
#                     "url": "table-datatable-jquery.html"
#                 },
#             ]
#         },
#         {
#             "separator": True,
#             "title": "Extra UI"
#         },
#         {
#             "title": "Widgets",
#             "icon": "pentagon-fill",
#             "sub_items": [
#                 {
#                     "title": "Chatbox", 
#                     "url": "ui-widgets-chatbox.html"
#                 },
#                 {
#                     "title": "Pricing", 
#                     "url": "ui-widgets-pricing.html"
#                 },
#                 {
#                     "title": "To-do List", 
#                     "url": "ui-widgets-todolist.html"
#                 },
#             ]
#         },
#         {
#             "title": "Icons",
#             "icon": "egg-fill",
#             "sub_items": [
#                 {
#                     "title": "Bootstrap Icons", 
#                     "url": "ui-icons-bootstrap-icons.html"
#                 },
#                 {
#                     "title": "Fontawesome", 
#                     "url": "ui-icons-fontawesome.html"
#                 },
#                 {
#                     "title": "Dripicons", 
#                     "url": "ui-icons-dripicons.html"
#                 },
#             ]
#         },
#         {
#             "title": "Charts",
#             "icon": "bar-chart-fill",
#             "sub_items": [
#                 {
#                     "title": "ChartJS", 
#                     "url": "ui-chart-chartjs.html"
#                 },
#                 {
#                     "title": "Apexcharts", 
#                     "url": "ui-chart-apexcharts.html"
#                 },
#             ]
#         },
#         {
#             "title": "File Uploader",
#             "url": "ui-file-uploader.html",
#             "icon": "cloud-arrow-up-fill",
#         },
#         {
#             "title": "Maps",
#             "icon": "map-fill",
#             "sub_items": [
#                 {
#                     "title": "Google Map", 
#                     "url": "ui-map-google-map.html"
#                 },
#                 {
#                     "title": "JS Vector Map", 
#                     "url": "ui-map-jsvectormap.html"
#                 },
#             ]
#         },
#         {
#             "title": "Multi-level Menu",
#             "icon": "three-dots",
#             "sub_items": [
#                 {
#                     "title": "First Level", 
#                     "url": "#",
#                     "sub_items": [
#                         {
#                             "title": "Second Level", 
#                             "url": "#"
#                         },
#                         {
#                             "title": "Second Level Menu", 
#                             "url": "#"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Another Menu", 
#                     "url": "#",
#                     "sub_items": [
#                         {
#                             "title": "Second Level Menu", 
#                             "url": "#"
#                         }
#                     ]
#                 },
#             ]
#         },
#         {
#             "separator": True,
#             "title": "Pages"
#         },
#         {
#             "title": "Email Application",
#             "url": "application-email.html",
#             "icon": "envelope-fill",
#         },
#         {
#             "title": "Chat Application",
#             "url": "application-chat.html",
#             "icon": "chat-dots-fill",
#         },
#         {
#             "title": "Photo Gallery",
#             "url": "application-gallery.html",
#             "icon": "image-fill",
#         },
#         {
#             "title": "Checkout Page",
#             "url": "application-checkout.html",
#             "icon": "basket-fill",
#         },
#         {
#             "title": "Authentication",
#             "icon": "person-badge-fill",
#             "sub_items": [
#                 {
#                     "title": "Login", 
#                     "url": "auth-login.html"
#                 },
#                 {
#                     "title": "Register", 
#                     "url": "auth-register.html"
#                 },
#                 {
#                     "title": "Forgot Password", 
#                     "url": "auth-forgot-password.html"
#                 },
#             ]
#         },
#         {
#             "title": "Errors",
#             "icon": "x-octagon-fill",
#             "sub_items": [
#                 {
#                     "title": "403", 
#                     "url": "error-403.html"
#                 },
#                 {
#                     "title": "404", 
#                     "url": "error-404.html"
#                 },
#                 {
#                     "title": "500", 
#                     "url": "error-500.html"
#                 },
#             ]
#         },
#         {
#             "separator": True,
#             "title": "Raise Support"
#         },
#         {
#             "title": "Documentation",
#             "icon": "life-preserver",
#             "url": "https://zuramai.github.io/mazer/docs"
#         },
#         {
#             "title": "Contribute",
#             "icon": "puzzle",
#             "url": "https://github.com/zuramai/mazer/blob/main/CONTRIBUTING.md"
#         },
#         {
#             "title": "Donate",
#             "icon": "cash",
#             "url": "https://github.com/zuramai/mazer#donation"
#         }
#     ]
# }

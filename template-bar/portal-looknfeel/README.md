### Template bar look & feel !

#### Portal Custom Stylesheet 

```css
.ods-dataset-images__image:after {
    font-size: 18px;
}
.odswidget-table__cell-container, .odswidget-table__header-cell-container {
    max-width: 600px;
}

/*************************************************************/
/* DEFAULT STYLESHEET 
/*
/* For fast customization, simply search for the COLORCOLOR word
/* and change the value related to your needs/customer chart
/*************************************************************/

/* GLOBAL */
.ods-box {
    border: none;   
    border-radius: 0px;
}

/* HEADER */ 

.ods-front-header {
    height: 175px; /* Increase header height */
    padding: 0;
}
.ods-front-header__menu-block {
    background-color: #427e9d; /* menu background color */ /* COLORCOLOR */
    width: 100%; /* get all the width of the screen */
}

.ods-front-header__portal-brand {
    height: 120px; /* increase brand block size containing brand name and logo */
    display: flex; /* display the logo then the brand name on the right */
    align-items: center; /* center the logo in the header */
    position: inherit;
}
.ods-front-header__portal-brand .ods-front-header__logo {
    height: 100px; /* increase logo size */
}
.ods-front-header__portal-brand__text {
    line-height: 100px; /* center text verticaly */
    font-weight: 600;    /* weight bold/regular etc... of the text header */
    font-size: 2.3rem; /* Size of the text header */
    color: #336179; /* Brand name color */ /* COLORCOLOR */
}

.ods-front-header__custom {
    position: absolute; 
    bottom: 0; /* Positionning to bottom of the header */
}
.ods-front-header__menu {
    white-space: nowrap; /* when screen is too small, don't break line let the menu items disapear on the right */
}   

.ods-front-header__menu-item { /* a menu item */
    display: inline-block;
    color: white; /* Color of the text of the item */ /* COLORCOLOR */
    background-color: #336179; /* Color of the background of the item when no mouse on it */ /* COLORCOLOR */
    margin: 0;
    margin-right: 2px; /* space between items, go to 0 for no space */
    height: 55px;
    text-align: center;
}
.ods-front-header__menu-item:hover { /* When mouse hover menu item */
    background-color: #427e9d; /* When the mouse go hover the item, the color change */ /* COLORCOLOR */
    text-shadow: 1px 1px 1px #000;
}
.ods-front-header__menu-item--active { /* item properties when an item is active, ie the current selected one */ 
    background-color: white; /* background color */ /* COLORCOLOR */
}
.ods-front-header__menu-item--active:hover { /* When mouse hover active items */
    background-color: white; /* background color when mouse hover */ /* COLORCOLOR */
    text-shadow: none;
}
.ods-front-header__menu-item-link { /* the link / text in the menu item */
    opacity: 1; /* Menu item link opcaity */
}
.ods-front-header__menu-item-link--active { /* when an item links is active, ie the current item */ 
    border-bottom: none; /* Remove the ODS bottom line when an item is active */
    color: #003958; /* Color of the text when the item is active */ /* COLORCOLOR */
    width: 100%;
}
.ods-front-header__menu-item-link--active:hover { /* when mouse is hover the active item links */ 
    border-bottom: none; /* Remove the ODS bottom line when an item is active */
    color: #003958; /* Color of the text when the item is active and mouse is hover it */ /* COLORCOLOR */
}
.ods-front-header__menu-item-link[href^="/page/home"]:before,
.ods-front-header__menu-item-link[href^="/page/accueil"]:before,
.ods-front-header__menu-item-link[href^="/pages/home"]:before,
.ods-front-header__menu-item-link[href^="/pages/accueil"]:before { /* Display the little home picto near the home page link item */
    font-family: "FontAwesome";
    content: '\f015'; /* Home picto, check here for others : http://fontawesome.io/icons/ */
    line-height: 1px; 
    font-size: 1.3em; /* size of the picto */
}

.ods-front-header__management-menu { /* Admin top right managment menu */
    right: 0;
    background-color: #427e9d; /* background color */ /* COLORCOLOR */
    line-height: 32px;
}

/* RESPONSIVE / MOBILE HEADER */

.ods-responsive-menu-placeholder__toggle {
    background-color: #336179; /* Hamburger menu color */ /* COLORCOLOR */
}
.ods-responsive-menu-placeholder__toggle:hover {
    background-color: #336179; /* Hamburger menu color */ /* COLORCOLOR */
}
.ods-responsive-menu-collapsible__toggle-button {
    color: black;
}
.ods-responsive-menu--collapsed .ods-front-header__portal-brand {
    display: inherit; 
}
.ods-responsive-menu--collapsed .ods-front-header__portal-brand .ods-front-header__logo {
    margin-top: 10px; /* positionning of the logo */
}
.ods-responsive-menu--collapsed {
    height: 120px; /* reduce the size of the header when displaying in mobile mode  */
    border-bottom: 2px solid #326078; /* little border to make a split between the logo and the page content */ /* COLORCOLOR */
}
.ods-responsive-menu-collapsible--collapsed .ods-front-header__menu { /* ignore it... just to make the display ok.... */
    width: 100%;
}
.ods-responsive-menu--collapsed .ods-front-header__menu-block .container { /* ignore it... just to make the display ok.... */
    padding-left: 0;
    padding-right: 0; 
    width: 100%; 
}
.ods-responsive-menu-collapsible--collapsed .ods-front-header__menu-item-link--active {
    border-left: none; /* Remove the ODS left line (repsonsive menu) when an item is active */
}

/* DATA CATALOG */

/* Every block */
.ods-filters__count,
.ods-filters__export-catalog-title, 
.ods-filters__filters, 
.ods-filters__filters-summary,
.ods-catalog-card,
.ods-tabs__pane.ods-tabs__pane--horizontal,
.odswidget-text-search__search-box,
.ods-tabs__tab.ods-tabs__tab--horizontal, 
.ods-tabs__tab.ods-tabs__tab--horizontal:hover
{
    border-radius: 0px; /* remove rounded border of almost every boxes on the platform */
}

/* DATA CATALOG DATASET CARD */
.ods-catalog-card__keyword { /* keywords items */
    border-radius: 0px;
    background-color: #003958; /* change de color of the keyword card block in the catalog */ /* COLORCOLOR */
}
.ods-catalog-card__keyword:hover { /* hover keyword item */
    background-color: #427e9d; /* color of the background when mouse hover the keyword block */ /* COLORCOLOR */
}


/* ANALYSIS VIEW */
.ods-chart-controls__yaxis { /* Analysis control block */
    background-color: white; /* background color, dirty grey by default */ /* COLORCOLOR */
}


/* FOOTER */
.ods-front-footer .portal-picto {
    height: 90px; /* Max size of the picto in the footer */
}
.ods-front-footer {
    border-top: 3px solid #427E9D; /* top line of the footer, delete if not needed */  /* COLORCOLOR */
    border-bottom: 3px solid #427E9D;  /* bottom line of the footer, delete if not needed */  /* COLORCOLOR */
    padding: 10px 0;
    height: auto;
}
.ods-front-footer__link {
    color: #427E9D;/* link color in the footer */  /* COLORCOLOR */   
}
```

#### Portal Custom Header 

```html
<nav class="ods-front-header" ods-responsive-menu breakpoint="1000">
    <ods-responsive-menu-placeholder>
        <a class="ods-front-header__portal-brand" href="/">
            ##logo##
        </a>
    </ods-responsive-menu-placeholder>
    <ods-responsive-menu-collapsible>
        <!-- BRAND AND LOGO Part -->
        <div class="ods-front-header__brand-block">
            <div class="container">
                <a class="ods-front-header__portal-brand" href="/">
                    ##logo##
                    ##brand##
                </a>
            </div>
        </div>
        <!-- NAVIGATION BAR -->
        <div class="ods-front-header__menu-block">
            <div class="container">
                ##menu##
            </div>
        </div>

        <!-- ADMIN MENU (top right) -->
        ##secondary-menu##
    </ods-responsive-menu-collapsible>
</nav>
```

#### Portal Custom Footer 

```html
<div class="ods-front-footer">
    <ods-theme-picto class="portal-picto"
                     theme="Discovery">
    </ods-theme-picto>
	##ods-logo## ##legal## ##language## <a href="#">ODSODSODS</a>
</div>
```


#### Result

[See it here !](https://template-discovery.opendatasoft.com/)
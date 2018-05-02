### PerfKPI look & feel !

#### Portal Custom Stylesheet 

```css
html {
}
h1, h2, h3, h4 {
    font-weight: bold;
    line-height: 1.25;
}
h1 {
    font-size: 2.4rem;
    line-height: 3rem;
}
h2 {
    font-size: 1.6rem;
    line-height: 2rem;    
}
h3 {
    font-size: 1.15rem;
    line-height: 2.2rem;
}
h4 {
    font-size: inherit;
}



/* HEADER */


/* BRAND AND LOGO LEFT BLOCK */
.perfkpi-header__container {
    display: flex;
    align-items: stretch;
    height: 80px;
}

.perfkpi-header__brand-link {
    display: inline-flex;   
}

.perfkpi-header__brand-link .theme-ods {
    height: 50px;
    margin: auto;
    width: 70px;
}

.perfkpi-header__brand-link:hover {
    text-decoration: none;
}




/* GLOBAL MENU */
 
.ods-front-header {
    height: 80px; /* CHANGE SIZE/HEIGHT HERE */
}
.ods-front-header__portal-brand__text {
    line-height: 80px;
    font-size: 2.3rem;
}
.perfkpi-header__ods {
    overflow: hidden;
}
.perfkpi-header__ods .ods-front-header__logo {
    height: 80px;
}

.perfkpi-header__perf {
    color: #003d64;
    line-height: 50px;
    margin-top: 10px;
    font-size: 1.4rem;
    font-weight: 300;
    margin-left: 20px;
    white-space: nowrap;
    font-style: italic;
}
.perfkpi-header__perf a {
    text-decoration: underline;
}
.perfkpi-header__perf a:hover {
    font-weight: 600;
}
@media (max-width: 600px) {
    .perfkpi-header__perf {
        /*display: none;*/
    }
}

.perfkpi-header__kpi {
    color: #003d64;
    line-height: 80px;
    font-size: 2.3rem;
    font-weight: 300;
    margin-left: 20px;
    white-space: nowrap;
    /*    border-right: 6px solid #003d64;
    border-left: 6px solid #0ABFBF;*/
    padding-right: 20px;
    padding-left: 20px;
}

.perfkpi-header__bloomberg-img {
    height: 26px;
    margin-top: 16px;
    margin-left: 20px;
}

/* 2 MENU VERSION : 1 in row, 1 in column */
/* MANAGEMENT MENU BELOW MAIN MENU */
.perfkpi-header__nav {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    text-align: right;
    text-transform: uppercase;
}

/* EVERYTHING ON THE SAME LINE */
/*.perfkpi-header__nav {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    display: flex;
    text-transform: uppercase; 
}*/




/* HEADER - management menu */

.ods-front-header__management-menu {
    position: relative;
    background-color: #0C518A;
    right: 0;
    display: flex;
}

.ods-front-header__management-menu-item {
    display: inline-flex;
    min-height: 35px;
    align-items: center;
    padding: 0;
    margin: 0;
}

.ods-front-header__management-menu-item-link {
    color: white;
    border-bottom: none;
    opacity: 1;
    position: relative;
    padding: 0 20px;
    height: 100%;
    display: inline-flex;
    align-items: center;
    transition: background-color 0.3s ease;
    font-size: 0.9rem;
}

.ods-front-header__management-menu-item-link i.fa {
    margin-right: 5px;
}

.ods-front-header__management-menu-item-link:hover {
    background-color: #0A4770; 
    border: none;
}

.ods-front-header__management-menu-item--backoffice {
    border-radius: 0;
}

.ods-front-header__management-menu-item-link--backoffice {
    background-color: #BF2257;
    color: #f8e273;    
    font-weight: 700;
}

.ods-front-header__management-menu-item-link--backoffice:hover {
    color: #BF2257;
    background-color: #f8e273;
}


.ods-front-header__account-avatar-container {
    margin: 0 5px 0 0;
}


/* HEADER - nav menu */

.ods-front-header__menu {
    margin: 0;
    padding: 0 10px;
    text-align: right;
    height: 100%;
}

.ods-front-header__menu-item {
    display: inline-flex;
    height: 100%;
    align-items: center;
    margin-left: 10px;
    margin-right: 10px;
}

.ods-front-header__menu-item-link {
    border-bottom: none;
    opacity: 1;
    position: relative;
    padding: 0;
    line-height: 1.3rem;
    font-weight: normal;
    font-size: 0.9rem;
}

.ods-front-header__menu-item-link:after {
    display: block;
    content: "";
    height: 1px;
    width: 0%;
    position: absolute;
    left: 0px;
    bottom: -4px;
    background: #003e65;
    -webkit-transition: width 0.3s ease;
    transition: width 0.3s ease;
}

.ods-front-header__menu-item-link--active:after {
    width: 100%;
}

.ods-front-header__menu-item-link:hover:after {
    width: 100%;
}

/* HEADER - Placeholder */

.ods-responsive-menu-placeholder__container {
    display: flex;
    align-items: stretch;
    justify-content: center;
    height: 80px;
}

.ods-responsive-menu-placeholder__container .perfkpi-header__perfkpi-img {
    border-right: none;
    padding-right: 0;

}

/* HEADER - Drawer */

.ods-responsive-menu-placeholder__toggle {
    /*border-left: 1px solid #0cbfbf;*/
    opacity: 1;
    transition: background-color 0.3s ease;
    font-size: 2.33rem;
    /*background-color: #0cbfbf7a;
    top: 80px;*/
    height: 100%;
}

.ods-responsive-menu-placeholder__toggle:hover {
    background-color: #0cbfbf;
}

.ods-responsive-menu-collapsible__toggle {
    padding: 0;
    border: none;
}

.ods-responsive-menu-collapsible__toggle-button {
    font-size: 1.33rem;
    height: 61px;
    width: 61px;
    line-height: 61px;
}

.ods-responsive-menu-collapsible__toggle-button:hover {
    color: #BD2658;
}

.ods-responsive-menu-collapsible--expanded .perfkpi-header__container {
    display: none;
}

.ods-responsive-menu-collapsible--expanded .perfkpi-header__nav {
    position: relative;
    flex-direction: column;
}

.ods-responsive-menu-collapsible__toggle {
    margin-bottom: 0;
}

.ods-responsive-menu-collapsible--expanded .ods-front-header__menu {
    padding: 0;
    margin: 0;
}

.ods-responsive-menu-collapsible--expanded .ods-front-header__menu-item {
    height: 50px;
    padding: 0;
    margin: 0;
    border-top: 1px solid rgba(255,255,255,0.2);
}

.ods-responsive-menu-collapsible--expanded .ods-front-header__menu-item-link {
    padding: 0 20px;
    border-left: 0;
    height: 49px;
    line-height: 49px;
    font-size: 0.9rem;
}

.ods-responsive-menu-collapsible--expanded .ods-front-header__menu-item-link:after {
    display: none;
}

.ods-responsive-menu-collapsible--expanded .ods-front-header__management-menu {
    flex-direction: column;    
    padding: 0;
}

.ods-responsive-menu-collapsible--expanded .ods-front-header__management-menu-item {
    padding: 0;
    margin: 0;
    height: 80px;
}

.ods-responsive-menu-collapsible--expanded .ods-front-header__management-menu-item-link {
    display: block !important;
    text-align: center;
    height: 80px;
    line-height: 80px;
    border: none !important;
}

.ods-responsive-menu-collapsible--expanded .ods-front-header__account-avatar-container {
    margin: 0 5px -7px 0;
    position: relative;
}
.ods-responsive-menu-collapsible--expanded .ods-front-header__account-avatar {
    position: absolute;
    top: 0;
    left: 0;
}

/* FOOTER */

.ods-front-footer {
    font-size: 0.9rem;
    text-align: left;
    height: 80px;
}

.ods-front-footer img {
    height: 20px;
    margin-right: 50px;
}

.ods-front-footer .container {
    height: 80px;
    display: flex;
    align-items: center;
}

.ods-front-footer .odswidget-theme-picto.theme-ods {
    height: 50px;
}

.ods-front-footer a {
    margin-right: 20px;
    color: #333;
}

.ods-front-footer a:hover {
    text-decoration: none;
    border-bottom: 1px solid #333;
    color: #000;
}

.ods-front-footer__legal {
    line-height: inherit;
    text-transform: uppercase;
    padding: 0;
}

/* EXPLORE CATALOG */

.ods-filters__filters {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}

.ods-filters__count, 
.ods-filters__export-catalog-title, 
.ods-filters__filters, 
.ods-filters__filters-summary,
.ods-filters-summary__count {
    font-size: 1.45rem;
    line-height: 1.72rem;
    border-left: 6px solid #F8E273;
    border-radius: 0;
    padding: 20px;
    font-weight: 500;
}

.ods-filters__sort {
    padding: 0;
    margin: 20px 0 20px 26px;
}

.odswidget-text-search {
    margin: 20px 0 20px 26px;
}

.ods-app-explore-catalog .odswidget-facet,
.ods-app-explore-dataset .odswidget-facet,
.ods-filters__export-catalog {
    margin: 20px 0 20px 26px;
}

.odswidget-facet__facet-title {
    font-size: 1.3rem;
    line-height: 2.15rem;
    font-weight: 500;

}

.odswidget-facet__category {
    border-left-color: transparent;
    padding: 5px 0 5px 10px;
    margin-left: -13px;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}

.ods-filters__export-catalog-link {
    border-left-color: transparent;
    padding: 5px 0 5px 10px;
    margin-left: -13px;
}

.ods-filters__export-catalog-link:hover,
.odswidget-facet__category:hover {
    color: #333;
}

.odswidget-facet__category--refined,
.odswidget-facet__category--refined:hover {
    color: #0C518A;
    font-weight: 500;
}

.odswidget-facet__value-icon {
    width: 1.4rem;
}

.odswidget-facet__category-count {
    font-size: 1rem;
    float: none;
    padding: 0;
    margin-left: 5px;
}

.ods-app-explore-catalog .odswidget-clear-all-filters,
.ods-app-explore-dataset .odswidget-clear-all-filters{
    position: static;
    right: initial;
    top: initial;
    font-size: 1.4rem;
}

.odswidget-geo-search {
    margin-left: 26px;
}

.odswidget-text-search__search-box {
    border-radius: 0;
    padding: 10px 30px 10px 10px;
    font-weight: 300;
    font-size: 1.4rem;
}

.odswidget-text-search__submit {
    padding: 0 10px;
    right: 0;
    font-size: 1.4rem;
}

@media screen and (min-width: 768px) {
    .ods-app-explore-catalog .ods-result-list {
        margin-left: 320px;
    }
}

/* EXPLORE CATALOG - Mobile */ 

@media screen and (max-width: 767px) {
    .ods-app-explore-catalog .ods-filters-placeholder,
    .ods-app-explore-dataset .ods-filters-summary {
        margin: -40px -40px -1px -40px;
    }

    .ods-filters__toggle-button,
    .ods-filters-summary__toggle {
        right: 40px;
        top: 38px;
    }

    .ods-app-explore-catalog .ods-filters,
    .ods-app-explore-dataset .ods-filters-summary {
        padding: 20px 40px;
    }
}



/* CATALOG CARD */

@media (min-width: 1200px) {
    .ods-catalog-card__wrapper {
        width: calc(50% - 20px);
    }
}

.ods-catalog-card {
    margin-bottom: 0;
    border-radius: 0;
    padding: 20px 20px 20px 0;
    border: none;
    border-top: 1px solid #EEE;
    transition: background 0.15s ease;
}

.ods-catalog-card:hover {
    background-color: #0C518A;
    color: #fff;
    padding: 20px 0 20px 20px;
    transition: padding 0.35s ease, background 0s;
}

.ods-catalog-card:hover .ods-catalog-card__title,
.ods-catalog-card:hover .ods-catalog-card__visualization {
    color: #fff;
}

.ods-catalog-card:hover .ods-catalog-card__theme-icon {
    fill: #fff;
}

.ods-catalog-card:hover:before {
    display: none;
}

.ods-catalog-card__title {
    font-size: 1.15rem;
    font-weight: bold;
}

.ods-catalog-card__visualizations {
    border-left: none;
}

.ods-catalog-card__visualization {
    padding: 0;
}

.ods-catalog-card__visualization:hover {
    text-decoration: underline;
}

.ods-catalog-card__title,
.ods-catalog-card__description,
.ods-catalog-card__metadata,
.ods-catalog-card__keywords {
    margin-left: 0;
}

.ods-catalog-card__header {
    display: flex;
}

.ods-catalog-card__theme-icon {
    position: static;
    margin-right: 1rem;
    fill: #333;
}

.ods-catalog-card__theme-icon svg,
.ods-catalog-card__theme-icon circle, 
.ods-catalog-card__theme-icon path, 
.ods-catalog-card__theme-icon polygon, 
.ods-catalog-card__theme-icon rect {
    fill: inherit !important;
}

/* for an unknown reason, I have to duplicate the theme icon in order for the catalog card to work, here I'm hiding the original one */
.ods-catalog-card > ods-catalog-card-theme-icon {
    display: none;
}



/* EXPLORE DATASET */

.ods-dataset-visualization__dataset-title {
    font-size: 3.4rem;
    color: #1A1A1A;
    margin: 0 0 40px 0;
}

.ods-dataset-metadata-block {
    font-size: inherit;
}

.ods-dataset-metadata-block__metadata-name {
    font-weight: 500;
}

.ods-app-explore-dataset .ods-filters {
    margin: 0 40px 40px 0;
}

@media screen and (max-width: 767px) {
    .ods-dataset-visualization__dataset-title {
        margin: 40px 0 !important;
    }
}

@media screen and (min-width: 768px) {
    .ods-app-explore-dataset .ods-dataset-visualization:not(.ods-dataset-visualization--full-width) {
        width: -webkit-calc(100% - 280px - 40px);
        width: calc(100% - 280px - 40px);
    }
}

.ods-dataset-export-link__explanations {
    font-size: 1rem;
}

.ods-dataset-export-link__format-name {
    font-weight: 500;
}

/* MISC */

main {
    margin: 40px 30px;    
    min-height: calc(100vh - 80px - 80px);
}


/* Tabs */

.ods-tabs__tabs {
    font-size: 1.15rem;
}


/* DATA VIZ */

.highcharts-background {
    fill: none;
}

.ods-chart {
    height: 300px;
}

.perfkpi-gauge--green .odswidget-gauge__svg-filler {
    stroke: #42A769;
}

.perfkpi-gauge--red .odswidget-gauge__svg-filler {
    stroke: #E95756;
}

```

Please not that there is two available versions in the CSS code. Just un comment the second header version to display the management menu in lined with the navigation menu.


#### Portal Custom Header 

```html
<nav class="ods-front-header" ods-responsive-menu breakpoint="768">
    <ods-responsive-menu-placeholder>
        <a class="perfkpi-header__brand-link" href="/">
            <div class="perfkpi-header__ods">
                ##logo##
            </div>
            <div class="perfkpi-header__kpi">
                ODS Village
            </div>
        </a>
    </ods-responsive-menu-placeholder>
    <ods-responsive-menu-collapsible>
        <div class="container perfkpi-header__container">
            <a class="perfkpi-header__brand-link" href="/">
                <div class="perfkpi-header__ods">
                    ##logo##
                </div>
                <div class="perfkpi-header__kpi">
                    ODS Village
                </div>
            </a>
        </div>
        <div class="perfkpi-header__nav">
            ##menu##
            ##secondary-menu##
        </div>
    </ods-responsive-menu-collapsible>
</nav>
```

#### Portal Footer 

```html
<div class="ods-front-footer">
    <div class="container">
        <ods-theme-picto theme="ODS"></ods-theme-picto>
         ##legal## ##language## 
    </div>
</div>
```


#### Result

[See it here !](https://perfkpi-odsplus.opendatasoft.com/)
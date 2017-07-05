### Template bar - home page #2 !

#### Code 

```html
<!--*************************************************************
 For fast customization, simply search for the word "ODSODSODS"
 and change the value related to your needs/customer chart
*************************************************************-->


<ods-catalog-context context="catalog">
    <div class="background">  
        <a class="explore-link" href="/explore/" target="_self">
            <i class="fa fa-search"></i>
            <span translate="">Explore datasets</span>
        </a>
        <ods-searchbox class="background_ods-searchbox" translate="placeholder" placeholder="Search datasets..."></ods-searchbox>
        <p>For example, 'ODSODSODS' or 'ODSODSODS'</p>
    </div>

    <div class="container body">
        <div class="row">
            <div class="col-md-6">
                <div class="ods-box body-content">
                    <h1>Welcome to the Open Data Portal of <strong>ODSODSODS</strong></h1>
                    <br/>
                    <p>  
                        ODSODSODS provides a data sharing platform that allows our organizations to make public data available and accessible to all residents. 
                    </p>
                    <p>
                        Our vision is to support a transformation that will lead to a simple, beautiful, and easy-to-use government. We built ODSODSODS to achieve this new, more effective, and open government.  
                    </p>
                </div>
            </div>
            <div class="col-md-6">
                <div class="row">

                    <div class="themeblock col-sm-6">
                        <div class="themeblock__content themeblock__content--a">
                            <div class="themeblock__icon">
                                <i class="fa fa-chain-broken"></i>
                            </div>
                            <h3>REGIONAL &amp; USEFUL</h3>
                            <p>
                                Data of ODSODSODS and its organizations. 
                            </p>

                        </div>
                    </div>

                    <div class="themeblock col-sm-6">
                        <div class="themeblock__content themeblock__content--b">
                            <div class="themeblock__icon">
                                <i class="fa fa-trophy"></i>
                            </div>
                            <h3>DATA QUALITY</h3>
                            <p>
                                Reliable data and semantic references through metadata.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="themeblock col-sm-6">
                        <div class="themeblock__content themeblock__content--c">
                            <div class="themeblock__icon">
                                <i class="fa fa-rocket"></i>
                            </div>
                            <h3>
                                INNOVATION AND ACCESS
                            </h3>        
                            <p>
                                We ecourage reuse by providing a robust API.
                            </p>
                        </div>
                    </div>
                    <div class="themeblock col-sm-6">
                        <div class="themeblock__content themeblock__content--d">
                            <div class="themeblock__icon">
                                <i class="fa fa-folder-open"></i>
                            </div>
                            <h3>
                                FREE AND OPEN DATA
                            </h3>
                            <p>
                                You are free to access and reuse our data.
                            </p>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        <div class="row" style="margin-top: 1em;">
            <div class="col-md-6">
                <div class="ods-box" style="border: none">
                    <h2 translate>Last modifications</h2>
                    <ods-last-datasets-feed context="catalog"></ods-last-datasets-feed>
                </div>
            </div>
            <div class="col-md-6">
                <div class="ods-box" style="border: none">
                    <h2 translate>Most popular data</h2>
                    <ods-most-popular-datasets context="catalog"></ods-most-popular-datasets>
                </div>
            </div>
        </div>
        <div class="map">
            <div class="map__description">
                <h2>ODSODSODS</h2>
                <p>
                    ODSODSODS
                </p>
                <ods-dataset-context context="ctx" 
                                     ctx-dataset="ODSODSODS">
                    <ods-map context="ctx">
                    </ods-map>
                </ods-dataset-context>
            </div>
        </div>
    </div>
</ods-catalog-context>
```

```css
/*************************************************************/
/* For fast customization, simply search for the COLOR word
/* and change the value related to your needs/customer chart
/*************************************************************/


main {
    margin: 0px 0px 20px 0px;
}

/* Background image and search bar */
.background {
    background-color: #f5f5f5; /* COLOR */
    background-image: url('/assets/theme_image/home3.png');
    background-position: center center;
    width: 100%;
    height: 400px;
    background-size: cover;
    text-align: center;
    color: #293E55; /* Text color on top of the background image, might change */ /* COLOR */
}
.background p {
    margin-top: -10px;
}
.container-fluid {
    padding-left: 0px;
    padding-right: 0px;
}
.explore-link {
    text-align: center;
    font-size: 1.8em;
    display: block;
    padding-top: 200px;
    padding-bottom: 20px;
    color: #293E55;  /* COLOR */
}
input.odswidget-searchbox__box {
    width: 80%;
    border: 2px solid white;
    border-radius: 5px;
    max-width: 550px;
    font-size: 1.5rem;
    line-height: 2rem;
    padding: 0.5em;
    font-family: "Open Sans";
}


/* Body content */
.body {
    margin-top: 20px;
}
.body-content {
    border: none;
    background-color: white;
}

/* Blocks */
.themeblock {
    color:black; /* COLOR */
    text-align: center;
    padding-bottom: 20px;
}
.themeblock h3 {
    color: #336179; /* COLOR */
    text-transform: uppercase;
}
.themeblock__icon {
    font-size: 3rem;
    color: #336179; /* COLOR */
}
.themeblock__content {
    background-color: white; /* COLOR */
    padding: 20px;
    display: block;
    color: inherit;
    text-decoration: none;
}
@media (min-width: 768px) and (max-width: 991px)  {
    .themeblock__content {
        min-height: 225px;
    }
}
@media (min-width: 992px) {
    .themeblock__content {
        min-height: 250px;
    }
}
.themeblock__content:hover {
    text-decoration: none;
}


/* Map dataviz */
.map {
    padding-top: 30px;
}
.map__description h2 {
    margin: 0 auto;
}
.map__description p {
    font-size: 12px;
}
```

#### Result

[See it here !](https://template-discovery.opendatasoft.com/pages/template2_home/)
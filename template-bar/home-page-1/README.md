### Template bar - home page #1 !

#### Code 

```html
<!--*************************************************************
 For fast customization, simply search for the word "ODSODSODS"
 and change the value related to your needs/customer chart
*************************************************************-->


<div class="container">
    <div class="header">
        <span class="copyright">© OpenDataSoft</span>
    </div>

    <div class="intro-block">
        <h2>Welcome to the Open Data Portal of ODSODSODS</h2>
        <p>
            On this portal, ODSODSODS publishes Open Data with the aim to increase the transparency for citizens and to collaborate with local developers.
        </p>   
        <a class="ods-button ods-button--primary" href="/explore/">
            <i class="fa fa-arrow-circle-o-right"></i>
            Explore! 
        </a>           
    </div>

    <ods-catalog-context context="catalog">
        <div class="row">

            <div class="themeblock col-md-3 col-sm-6">
                <div class="themeblock__content themeblock__content--a">
                    <div class="themeblock__icon">
                        <i class="fa fa-chain-broken"></i>
                    </div>
                    <h3>TRANSPARENCY</h3>
                    <p>
                        Data of ODSODSODS and its organizations.
                    </p>
                </div>
            </div>

            <div class="themeblock col-md-3 col-sm-6">
                <div class="themeblock__content themeblock__content--b">
                    <div class="themeblock__icon">
                        <i class="fa fa-trophy"></i>
                    </div>
                    <h3>QUALITY</h3>
                    <p>
                        Reliable data and semantic references through metadata.
                    </p>
                </div>
            </div>
            <div class="themeblock col-md-3 col-sm-6">
                <div class="themeblock__content themeblock__content--c">
                    <div class="themeblock__icon">
                        <i class="fa fa-rocket"></i>
                    </div>
                    <h3>
                        INNOVATION &amp; ACCESS
                    </h3>        
                    <p>
                        We ecourage reuse by providing a robust API.
                    </p>
                </div>
            </div>
            <div class="themeblock col-md-3 col-sm-6">
                <div class="themeblock__content themeblock__content--d">
                    <div class="themeblock__icon">
                        <i class="fa fa-folder-open"></i>
                    </div>
                    <h3>
                        OPEN &amp; FREE DATA
                    </h3>
                    <p>
                        You are free to access and reuse our data.
                    </p>
                </div>
            </div>

        </div>
        <div class="row">
            <div class="col-md-6">

                <div class="themeblock">
                    <div class="themeblock__content themeblock__content--b">
                        <div class="themeblock__icon">
                            <i class="fa fa-download"></i>
                        </div> 
                        <h3>
                            LAST 5 UPDATES
                        </h3>
                        <span style="text-align:left">
                            <ods-last-datasets-feed context="catalog"></ods-last-datasets-feed>
                        </span>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="themeblock">
                    <div class="themeblock__content themeblock__content--b">
                        <div class="themeblock__icon">
                            <i class="fa fa-download"></i>
                        </div> 
                        <h3>
                            TOP 5 DOWNLOADS
                        </h3>
                        <span style="text-align:left">
                            <ods-most-popular-datasets context="catalog"></ods-most-popular-datasets>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </ods-catalog-context>

</div>
```

```css
/*************************************************************/
/* For fast customization, simply search for the COLOR word
/* and change the value related to your needs/customer chart
/*************************************************************/


/* Background picture */
.header {
    background-image: url("/assets/theme_image/home3.png");
    background-color: white;
    background-position: top center;
    background-size: cover;
    margin: -20px -40px 0 -40px;
    padding: 230px 0;
    position: relative;
    color: white; /* COLOR */
}
.copyright {
    position: absolute;
    bottom: 0px;
    right: 2px;
    text-shadow: 1px 1px #000;
}

/* INTRO Over the picture */
.intro-block {
    color: white; /* COLOR */
    background-color: rgba(0,57,88,0.8);
    max-width: 550px;
    padding: 20px 40px 25px 40px;
    position: relative;
    margin-top: -125px;
}
.intro-block h2 {
    color: white; /* COLOR */
}


/* BLOCKS */ 
.themeblock {
    color:black; /* COLOR */
    text-align: center;
    padding-top: 20px;
}
.themeblock h3 {
    color: rgb(0,57,88); /* COLOR */
    text-transform: uppercase;
}
.themeblock p {
    color: rgb(0,57,88); /* COLOR */
}
.themeblock__icon {
    font-size: 3rem;
    color: rgb(0,57,88); /* COLOR */
}
.themeblock__content {
    padding: 20px;
    display: block;
    text-decoration: none;
    border-radius: 0px;
    border: 2px solid rgb(0,57,88); /* COLOR */
    background-color: #f2f2f2; /* COLOR */
}
.themeblock__content:hover {
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
```

#### Result

[See it here !](https://template-discovery.opendatasoft.com/pages/template1_home/)
### Template bar - datastory #1 !

#### First, the result !

[See the template here !](https://template-discovery.opendatasoft.com/pages/datastory1/)
[See an example here !](https://template-discovery.opendatasoft.com/pages/datastory1_example/)

#### Then, some explanations of all subsets of codes !

##### Blocks

  * White background block
```html
<!-- ONE BLOCK WITH WHITE BACKGROUND -->
    <div class="row white-block" >
        ...
    </div>
<!-- ONE BLOCK WITH WHITE BACKGROUND END -->
```

  * Light grey background block
```html

<!-- ONE BLOCK WITH GREY BACKGROUND -->
    <div class="row grey-block" >
        ...
    </div>
<!-- ONE SECTION WITH GREY BACKGROUND -->
```



##### Title and subtitle of a block 

  * Title of the block
```html
<h1 class="block-title">
    SET BLOCK TITLE HERE
</h1>
```

  * Subtitle of the block
```html
<h2 class="block-subtitle">
    SET BLOCK SUB-TITLE HERE
</h2>
```

##### Then, different sections in the block

  * A double columns text section 
```html
<!-- TEXT SECTION WITH 2 COUMNS -->            
            <div class="col-md-6 block-section-text block-section-text-left">
                SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE
            </div>
            <div class="col-md-6 block-section-text">
                SET TEXT CONTENT HERE
                <a href="#">EXTERNAL LINK EXEMPLE <i class="fa fa-external-link" aria-hidden="true"></i></a>
                SET TEXT CONTENT HERE
                <a href="#">INTERNAL LINK EXEMPLE</a>
            </div>
<!-- TEXT SECTION WITH 2 COUMNS END -->    
```

  * A two-third / one-third split for a chart and a link or some text on the side
```html
<!-- CHART SECTION WITH LINK 2/3 1/3 -->
            <div class="col-md-8 block-section-chart">
                -- REPLACE THIS BY THE CHART WIDGET CODE -- 
            </div>
            <div class="col-md-4 block-section-text">
                <a href="#">LINK TO THE DATASET <i class="fa fa-external-link" aria-hidden="true"></i></a>
            </div>
<!-- CHART SECTION WITH LINK 2/3 1/3 END -->
```

  * A text section filling all the width of the page
```html
<!-- TEXT SECTION WITH 1 COLUMN -->            
            <div class="col-md-12 block-section-text block-section-text-left">
                SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE
                <a href="#">EXTERNAL LINK EXEMPLE <i class="fa fa-external-link" aria-hidden="true"></i></a>
                SET TEXT CONTENT HERE
                <a href="#">INTERNAL LINK EXEMPLE</a>
            </div>
<!-- TEXT SECTION WITH 1 COLUMN END -->  
``` 

  * A chart section filling all the wisth of the page
```html
<!-- CHART SECTION FULL WIDTH -->
            <div class="col-md-12 block-section-chart">
                -- REPLACE THIS BY THE CHART WIDGET CODE -- 
            </div>
<!-- CHART SECTION FULL WIDTH END -->
```


#### Finally, the full code 

```html
<!-- DASHBOARD -->
<div class="container-fluid dashboard">

    <!-- DASHBOARD TITLE -->
    <div class="row grey-block" >
        <div class="col-md-3 header-img">
            <img alt="dashboard logo" src="/assets/theme_image/picture_here.png" />
        </div>
        <div class="col-md-6">
            <div class="header-title">
                SET TITLE HERE
            </div>
            <div class="header-subtitle">
                <h1>
                    SET SUB-TITLE HERE
                </h1>
            </div>
        </div>
    </div>
    <!-- END OF DASHBOARD TITLE -->



    <!-- ONE BLOCK WITH WHITE BACKGROUND -->
    <div class="row white-block" >

        <h1 class="block-title">
            SET BLOCK TITLE HERE
        </h1>
        <h2 class="block-subtitle">
            SET BLOCK SUB-TITLE HERE
        </h2>

        <!-- SECTION CONTENT -->
        <div class="row block-section">

            <!-- TEXT SECTION WITH 2 COUMNS -->            
            <div class="col-md-6 block-section-text block-section-text-left">
                SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE
            </div>
            <div class="col-md-6 block-section-text">
                SET TEXT CONTENT HERE
                <a href="#">EXTERNAL LINK EXEMPLE <i class="fa fa-external-link" aria-hidden="true"></i></a>
                SET TEXT CONTENT HERE
                <a href="#">INTERNAL LINK EXEMPLE</a>
            </div>
            <!-- TEXT SECTION WITH 2 COUMNS END -->     


            <!-- CHART SECTION WITH LINK 2/3 1/3 -->
            <div class="col-md-8 block-section-chart">
                -- REPLACE THIS BY THE CHART WIDGET CODE -- 
            </div>
            <div class="col-md-4 block-section-text">
                <a href="#">LINK TO THE DATASET <i class="fa fa-external-link" aria-hidden="true"></i></a>
            </div>
            <!-- CHART SECTION WITH LINK 2/3 1/3 END -->

            <!-- TEXT SECTION WITH 1 COLUMN -->            
            <div class="col-md-12 block-section-text block-section-text-left">
                SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE
                <a href="#">EXTERNAL LINK EXEMPLE <i class="fa fa-external-link" aria-hidden="true"></i></a>
                SET TEXT CONTENT HERE
                <a href="#">INTERNAL LINK EXEMPLE</a>
            </div>
            <!-- TEXT SECTION WITH 1 COLUMN END -->  

            <!-- CHART SECTION FULL WIDTH -->
            <div class="col-md-12 block-section-chart">
                -- REPLACE THIS BY THE CHART WIDGET CODE -- 
            </div>
            <!-- CHART SECTION FULL WIDTH END -->

        </div>
        <!-- SECTION CONTENT END-->

    </div>
    <!-- ONE BLOCK WITH WHITE BACKGROUND END -->


    <!-- ONE BLOCK WITH GREY BACKGROUND -->
    <div class="row grey-block" >

        <h1 class="block-title">
            SET BLOCK TITLE HERE
        </h1>
        <h2 class="block-subtitle">
            SET BLOCK SUB-TITLE HERE
        </h2>

        <!-- SECTION CONTENT -->
        <div class="row block-section">

            <!-- TEXT SECTION WITH 1 COLUMN -->            
            <div class="col-md-12 block-section-text block-section-text-left">
                SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE
                <a href="#">EXTERNAL LINK EXEMPLE <i class="fa fa-external-link" aria-hidden="true"></i></a>
                SET TEXT CONTENT HERE
                <a href="#">INTERNAL LINK EXEMPLE</a>
            </div>
            <!-- TEXT SECTION WITH 1 COLUMN END -->

            <!-- TEXT SECTION WITH 2 COUMNS -->            
            <div class="col-md-6 block-section-text block-section-text-left">
                SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE
            </div>
            <div class="col-md-6 block-section-text">
                SET TEXT CONTENT HERE
                <a href="#">EXTERNAL LINK EXEMPLE <i class="fa fa-external-link" aria-hidden="true"></i></a>
                SET TEXT CONTENT HERE
                <a href="#">INTERNAL LINK EXEMPLE</a>
            </div>
            <!-- TEXT SECTION WITH 2 COUMNS END -->     
        </div>
        <!-- SECTION CONTENT END-->

        
        <h2 class="block-subtitle">
            SET BLOCK SUB-TITLE HERE
        </h2>

        <!-- SECTION CONTENT -->
        <div class="row block-section">

            <!-- TEXT SECTION WITH 2 COUMNS -->            
            <div class="col-md-6 block-section-text block-section-text-left">
                SET TEXT CONTENT HERE ### SET TEXT CONTENT HERE
            </div>
            <div class="col-md-6 block-section-text">
                SET TEXT CONTENT HERE
                <a href="#">EXTERNAL LINK EXEMPLE <i class="fa fa-external-link" aria-hidden="true"></i></a>
                SET TEXT CONTENT HERE
                <a href="#">INTERNAL LINK EXEMPLE</a>
            </div>
            <!-- TEXT SECTION WITH 2 COUMNS END -->     

        </div>
        <!-- SECTION CONTENT END-->

    </div>
    <!-- ONE SECTION WITH GREY BACKGROUND -->

</div>
```

```css
.dashboard {
    margin: -10px;
    margin-top: -20px;
}

.grey-block {
    background-color: whitesmoke;
    padding: 15px 60px;
}
.white-block {
    background-color: white;
    padding: 15px 60px;
}
.header-img {
    text-align: center;
}
.header-img img {
    width: 250px;
    height: 250px;
    padding: 25px;
}
.header-title {
    text-align: center;
    font-size: 4em;
    font-weight: 300;
    line-height: 1em;
    margin: 50px 0 10px 0;
    color: darkred;
}
.header-subtitle {
    text-align: center;
    margin-bottom: 30px;
}
.header-subtitle h1 {
    font-weight: 300;
    color: darkred;
}
.header-subtitle h1:before, .header-subtitle h1:after {
    width: 75px;
    height: 1px;
    background-color: darkred;
    content: '';
    display: block;
    vertical-align: middle;
    margin: 20px auto;
}


.block-section {
    margin: 50px 0px;
}
.block-title {
    text-align: center;
    font-weight: 500;
    font-size: 3em;
    margin-top: 35px !important;
    color: darkred;
}
.block-subtitle {
    text-align: center;
    width: 70%;
    margin: 10px auto;
    color: darkred;
    font-weight: 300;
}
.block-section-text {
    padding: 0 35px;
    margin: 35px 0;
    text-align: justify;
    font-size: 1.3em;
    font-weight: 300;
}
.block-section-text-left {
    border-right: 1px darkred solid;
}
.block-section-text a {
    color: darkred;
    font-weight: 500;
}

rect.highcharts-background {
    fill: rgba(0, 0, 0, 0) !important;
}
```

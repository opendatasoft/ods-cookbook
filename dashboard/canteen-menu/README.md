### School canteen menu

#### Live demo

[Please find the live exemple on Discovery](https://discovery.opendatasoft.com/pages/menu-cantine/)

#### Code

HTML code :

```html
<ods-dataset-context context="menuscantines" 
                     menuscantines-dataset="menus-cantines" 
                     menuscantines-domain="rennes-metropole"
                     menuscantines-parameters="{'sort':'-date','refine.secteur':'1'}"
                     ng-init="weekselect = 0">

    {{ menuscantines.parameters['q'] = "date:[#now(weeks=" + (weekselect - 1) + ",weekday=6) TO #now(weeks=" + (weekselect) + ",weekday=4)]"; ""
    }}

    <div class="weeks-selects">
        <div class="week-select" ng-class="{'week-selected': weekselect == -1}"
             ng-click="weekselect = -1">
            Past week
        </div>
        <div class="week-select" ng-class="{'week-selected': weekselect == 0}"
             ng-click="weekselect = 0">
            Current week
        </div>
        <div class="week-select" ng-class="{'week-selected': weekselect == 1}"
             ng-click="weekselect = 1">
            Next week
        </div>
    </div>

    <div class="container app">
        <div>
            <ul class="menus">
                <li>
                    <div class="ods-box header">
                        <div class="logos">
                            <img src="/assets/theme_image/rennes_logo.png" />
                        </div>
                        <h1>
                            School canteen menu <br/>
                            City of Rennes
                        </h1>
                        <div class="row items">
                            <div class="item type">
                                <h2>
                                    Starter
                                </h2>  
                            </div>
                            <div class="item type">
                                <h2>
                                    Main course
                                </h2>  
                            </div>
                            <div class="item type">
                                <h2>
                                    Vegetables
                                </h2>  
                            </div>
                            <div class="item type">
                                <h2>
                                    Dairy
                                </h2>  
                            </div>
                            <div class="item type">
                                <h2>
                                    Desert
                                </h2>  
                            </div>
                            <div class="item type">
                                <h2>
                                    Snack
                                </h2>  
                            </div>
                        </div>
                    </div>
                </li>
                <li ng-repeat="menu in menus"
                    ods-results="menus"
                    ods-results-context="menuscantines"
                    class="menu">
                    <div class="ods-box">
                        <h2>
                            <span class="stronger">{{ menu.fields.date | date : 'fullDate' | capitalize }}</span>
                        </h2>
                        <div class="row items">
                            <div class="item plat">
                                <h3>
                                    {{ menu.fields.entree }}
                                </h3>
                                <div class="item logo">
                                    <!--h3>
                                    {{ menu.fields.code_entree }}
                                </h3-->  
                                    <img ng-if="menu.fields.code_entree.indexOf('AB') >= 0" src="/assets/theme_image/ab.png" />
                                    <img ng-if="menu.fields.code_entree.indexOf('VBF') >= 0" src="/assets/theme_image/vbf.png" />
                                    <img ng-if="menu.fields.code_entree.indexOf('VPF') >= 0" src="/assets/theme_image/vpf.png" />
                                    <img ng-if="menu.fields.code_entree.indexOf('EBR') >= 0" src="/assets/theme_image/ebr.jpg" />
                                </div>
                            </div>
                            <div class="item plat">
                                <h3>
                                    {{ menu.fields.plat }}
                                </h3>
                                <div class="item logo">
                                    <!--h3>
                                    {{ menu.fields.code_plat }}
                                </h3-->  
                                    <img ng-if="menu.fields.code_plat.indexOf('AB') >= 0" src="/assets/theme_image/ab.png" />
                                    <img ng-if="menu.fields.code_plat.indexOf('VBF') >= 0" src="/assets/theme_image/vbf.png" />
                                    <img ng-if="menu.fields.code_plat.indexOf('VPF') >= 0" src="/assets/theme_image/vpf.png" />
                                    <img ng-if="menu.fields.code_plat.indexOf('EBR') >= 0" src="/assets/theme_image/ebr.jpg" />
                                </div>
                            </div>
                            <div class="item plat">
                                <h3>
                                    {{ menu.fields.legumes }}
                                </h3>
                                <div class="item logo">
                                    <!--h3>
                                    {{ menu.fields.code_legumes }}
                                </h3-->  
                                    <img ng-if="menu.fields.code_legumes.indexOf('AB') >= 0" src="/assets/theme_image/ab.png" />
                                    <img ng-if="menu.fields.code_legumes.indexOf('VBF') >= 0" src="/assets/theme_image/vbf.png" />
                                    <img ng-if="menu.fields.code_legumes.indexOf('VPF') >= 0" src="/assets/theme_image/vpf.png" />
                                    <img ng-if="menu.fields.code_legumes.indexOf('EBR') >= 0" src="/assets/theme_image/ebr.jpg" />
                                </div>
                            </div>
                            <div class="item plat">
                                <h3>
                                    {{ menu.fields.laitage }}
                                </h3>
                                <div class="item logo">
                                    <!--h3>
                                    {{ menu.fields.code_laitage }}
                                </h3-->  
                                    <img ng-if="menu.fields.code_laitage.indexOf('AB') >= 0" src="/assets/theme_image/ab.png" />
                                    <img ng-if="menu.fields.code_laitage.indexOf('VBF') >= 0" src="/assets/theme_image/vbf.png" />
                                    <img ng-if="menu.fields.code_laitage.indexOf('VPF') >= 0" src="/assets/theme_image/vpf.png" />
                                    <img ng-if="menu.fields.code_laitage.indexOf('EBR') >= 0" src="/assets/theme_image/ebr.jpg" />
                                </div>
                            </div>
                            <div class="item plat">
                                <h3>
                                    {{ menu.fields.dessert }}
                                </h3>
                                <div class="item logo">
                                    <!--h3>
                                    {{ menu.fields.code_dessert }}
                                </h3-->  
                                    <img ng-if="menu.fields.code_dessert.indexOf('AB') >= 0" src="/assets/theme_image/ab.png" />
                                    <img ng-if="menu.fields.code_dessert.indexOf('VBF') >= 0" src="/assets/theme_image/vbf.png" />
                                    <img ng-if="menu.fields.code_dessert.indexOf('VPF') >= 0" src="/assets/theme_image/vpf.png" />
                                    <img ng-if="menu.fields.code_dessert.indexOf('EBR') >= 0" src="/assets/theme_image/ebr.jpg" />
                                </div>
                            </div>
                            <div class="item plat">
                                <h3>
                                    {{ menu.fields.gouter }}
                                </h3>
                                <div class="item logo">
                                    <!--h3>
                                    {{ menu.fields.code_gouter }}
                                </h3-->  
                                    <img ng-if="menu.fields.code_gouter.indexOf('AB') >= 0" src="/assets/theme_image/ab.png" />
                                    <img ng-if="menu.fields.code_gouter.indexOf('VBF') >= 0" src="/assets/theme_image/vbf.png" />
                                    <img ng-if="menu.fields.code_gouter.indexOf('VPF') >= 0" src="/assets/theme_image/vpf.png" />
                                    <img ng-if="menu.fields.code_gouter.indexOf('EBR') >= 0" src="/assets/theme_image/ebr.jpg" />
                                </div>
                            </div>
                        </div>
                        <div class="row items">






                        </div>
                    </div>
                </li>
            </ul>
        </div>             

        <!--div id="debug">
            <br/>        <br/>        <br/>        <br/>        <br/>        <br/>        <br/>

            <h2>
                Debug view
            </h2>
            <h3>
                Query : {{ menuscantines.parameters['q'] }}
            </h3>
            <div class="ods-box">
                <ods-table context="menuscantines" sort="-date"></ods-table>
            </div>
        </div-->
    </div>
</ods-dataset-context>

```

CSS code: 

```css
.ods-box {
    padding: 10px;
    margin-bottom: 15px;
}

.app {
    max-width: 760px;
}

ul {
    list-style: none;
}

.header {
    position: relative;
}
.logos {
    position: absolute;
    right: 15px;
}
.logos img:nth-child(1) {
    height: 50px;
}
/*.logos img:nth-child(2) {
position: absolute;
right: 0;
width: 149px;
height: 49px;
}*/

.menus {
    text-align: center;
}
h1 {
    margin: 0px 0px 30px 15px;
    text-align: left;
    margin-top: 3px;
}
.menu h2 {
    margin-bottom: 15px;
    font-size: 1.2em;
}
.items {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}
.type {
    margin: 0px 5px;
}
.logo {
    width: 110px;
}
.logo img {
    max-height: 30px;
    max-width: 30px;
}
.item.type h2 {
    width: 105px;
}
.item.plat h3 {
    width: 110px;
    font-size: 1.1em;
}
.stronger {
    font-weight: 400;
}

.weeks-selects {
    display: flex;
    justify-content: center;
}
.week-select {
    padding: 5px 0;
    margin: 5px;
    border: 1px solid #1f0d3340;
    width: 201px;
    text-align: center;
}
.week-select:hover {
    border-bottom: 1px solid #1f0d33;
}
.week-selected {
    border-color: #1f0d33;
    font-weight: 500;
    background-color: white;
}

@media print {
    header, footer, #debug, .weeks-selects {
        display: none;
    }
    .ods-box.header {
        border: none;
    }
}
```

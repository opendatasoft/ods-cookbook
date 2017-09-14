### Template bar - datastory #2 !

#### See live demo !

  * [Template bar demo here !](https://template-discovery.opendatasoft.com/pages/datastory2/)
  
#### The full code 

```html
<div class="datastory">
    <div class="container container--header">
        <h1>Data story title</h1>

        <p class="tagline">Proinde concepta rabie saeviore, quam desperatio incendebat et fames, amplificatis viribus ardore incohibili in excidium urbium matris Seleuciae efferebantur, quam comes tuebatur Castricius tresque legiones bellicis sudoribus induratae.</p>

        <p class="intro">Ex his quidam aeternitati se commendari posse per statuas aestimantes eas ardenter adfectant quasi plus praemii de figmentis aereis sensu carentibus adepturi, quam ex conscientia honeste recteque factorum, easque auro curant inbracteari, quod Acilio Glabrioni delatum est primo, cum consiliis armisque regem superasset Antiochum. quam autem sit pulchrum exigua haec spernentem et minima ad ascensus verae gloriae tendere longos et arduos, ut memorat vates Ascraeus, Censorius Cato monstravit. qui interrogatus quam ob rem inter multos... statuam non haberet malo inquit ambigere bonos quam ob rem id non meruerim, quam quod est gravius cur inpetraverim mussitare.</p>

    </div>

    <div class="container container--body">
        <h2>A block</h2>

        <p>Adolescebat autem obstinatum propositum erga haec et similia multa scrutanda, stimulos admovente regina, quae abrupte mariti fortunas trudebat in exitium praeceps, cum eum potius lenitate feminea ad veritatis humanitatisque viam reducere utilia suadendo deberet, ut in Gordianorum actibus factitasse Maximini truculenti illius imperatoris rettulimus coniugem.</p>

        <h2>A block with list</h2>

        <p>Nemo quaeso miretur, si post exsudatos labores itinerum longos congestosque adfatim commeatus fiducia vestri ductante barbaricos pagos adventans velut mutato repente consilio ad placidiora deverti.</p>

        <ul>
            <li>Nemo quaeso miretur, si post exsudatos labores itinerum longos congestosque.</li>
            <li>adfatim commeatus fiducia vestri ductante barbaricos pagos adventans velut mutato repente consilio ad placidiora deverti.</li>
        </ul>      

        <h2>A block with picture and link</h2>

        <img src="/assets/theme_image/home.png" style="align : center; width: 100%">

        <p>
            Ut enim benefici liberalesque sumus, non ut exigamus gratiam (neque enim beneficium faeneramur sed natura propensi ad liberalitatem sumus), sic amicitiam non spe mercedis adducti sed quod omnis eius fructus in ipso amore inest, expetendam putamus.
        </p>

        <p>
            <a href="#">Lorem ipsum !</a>
        </p>

        <h2>A block with live data vizualisation</h2>

        <p>Adolescebat autem obstinatum propositum erga haec et similia multa scrutanda, stimulos admovente regina, quae abrupte mariti fortunas trudebat in exitium praeceps, cum eum potius lenitate feminea ad veritatis humanitatisque viam reducere utilia suadendo deberet, ut in Gordianorum actibus factitasse Maximini truculenti illius imperatoris rettulimus coniugem.</p>

        <ods-dataset-context context="recordstores" recordstores-dataset="record-stores">
            <ods-chart single-y-axis="true">
                <ods-chart-query context="recordstores" field-x="city" maxpoints="20" sort="serie1-1">
                    <ods-chart-serie expression-y="supporter" chart-type="area" function-y="COUNT" color="#19630A" scientific-display="true">
                    </ods-chart-serie>
                    <ods-chart-serie expression-y="ratecnt" chart-type="line" function-y="SUM" color="#BA022A" scientific-display="true">
                    </ods-chart-serie>
                </ods-chart-query>
            </ods-chart>

        </ods-dataset-context>

    </div>
</div>
```

```css
.datastory {
    background-color: white;
    margin: -20px -10px;
    padding-top: 40px;
}

.datastory .container--header {
    max-width: 1000px;
    font-size: 1.2rem;
}

.datastory .container--body {
    max-width: 750px;
    margin-top: 60px;
}

.datastory h1{
    text-align:center;
    font-size: 3em;
    font-weight: 200;
}

.datastory h2 {
    border-left: 3px solid #007B9C;
    padding-left: 12px;
    font-weight: 400;
}

.datastory ul,
.datastory p {
    font-size: 1.33em;
    line-height: 1.5em;
    margin-left: 15px;
    font-weight: 200;
}
.secondary-list-item {
    font-size: 0.75em; 
    line-height: 1.5em;
}
.primary-list-item {
    font-size: 1.33em; 
    line-height: 1.5em;
}
.datastory .tagline {
    text-align: center;
    font-style: italic;
    margin-top: 20px;
    margin-bottom: 40px;
    font-weight: 300;
}

@media (min-width: 768px) {
    .datastory .intro {
        text-align: justify;   
    }
}
```

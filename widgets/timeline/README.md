### Timeline custom view

[Live exemple here] (https://discovery.opendatasoft.com/explore/dataset/les-grandes-dates-dissy-les-moulineaux/timeline/)

This custom view is an interesting way to present data sorted by date and highlighting details about an event, a person or a story.

It's simply the usage of `ods-infinite-scroll-results` widget.
Plus CSS styles to display it like a timeline from top to the bottom

```html
{{ ctx.parameters['sort'] = 'annee' ; "" }}

<ods-infinite-scroll-results context="ctx" 
                             scroll-top-when-refresh="false"
                             list-class="timeline-frame"
                             result-class="timeline-item"
                             no-results-message="No more event...">

    {{ url = '/explore/dataset/' + item.datasetid + '/files/' + item.fields.imagecsv.id + '/300/' ; "" }}

    <div class="timeline-img" style=""></div>

    <div class="timeline-content timeline-card">
        <div class="timeline-img-header"
             ng-class="{'no-img' : !item.fields.imagecsv}"
             style="{{ 'background: linear-gradient(rgba(0,0,0,0), rgba(0,0,0, .4)), url(' + url + ') center center no-repeat;
                    background-size: cover;' }}">
            <h2>{{ item.fields.evenement }}</h2>
        </div>

        <div class="date">
            <span ng-if="item.fields.jour">{{ item.fields.jour }} </span>
            <span ng-if="item.fields.mois"> {{item.fields.mois }} </span>
            {{ item.fields.annee }}
        </div>
        <p>{{ item.fields.description }}</p>
        <div class="timeline-bottom">
            <a class="bnt-more"
               target="_blank"
               ng-href="{{ item.fields.web }}">En savoir plus <i class="fa fa-external-link" aria-hidden="true"></i></a>
            <div class="timeline-geo">
                <i class="fa fa-map-marker" aria-hidden="true"></i>
                <ods-geotooltip coords="item.fields.coordonnees_geo"
                                record="item"
                                width="300"
                                height="300">
                    {{ item.fields.numero }} {{ item.fields.adresse }}<br/>{{ item.fields.ville }}
                </ods-geotooltip>
            </div>
        </div>
    </div>

</ods-infinite-scroll-results>
```



```css

.timeline-frame {
    position: relative;
}
.timeline-frame:before {
    content: '';
    background: #1C0F31;
    width: 5px;
    height: 95%;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);

}

.timeline-item {
    width: 100%;
    margin-bottom: 70px;
}
.timeline-item:nth-child(even) .timeline-content {
    float: right;
    padding: 40px 30px 10px 30px;
}
.timeline-item:nth-child(even) .timeline-content .date {
    right: auto;
    left: 0;
}
.timeline-item:nth-child(even) .timeline-content .date:after {
    content: '';
    position: absolute;
    border-style: solid;
    width: 0;
    height: 0;
    top: 30px;
    left: -15px;
    border-width: 10px 15px 10px 0;
    border-color: transparent #1d0f31 transparent transparent;
}
.timeline-item:after {
    content: '';
    display: block;
    clear: both;
}

.timeline-content {
    position: relative;
    width: 45%;
    padding: 10px 30px;
    border-radius: 4px;
    background: #f5f5f5;
    box-shadow: 0 20px 25px -15px rgba(0, 0, 0, .3);
}

.timeline-item:nth-child(odd) .timeline-content:after  {
    content: '';
    position: absolute;
    border-style: solid;
    width: 0;
    height: 0;
    top: 30px;
    right: -15px;
    border-width: 10px 0 10px 15px;
    border-color: transparent transparent transparent #1d0f31;
}

.timeline-img {
    width: 30px;
    height: 30px;
    background: white;
    border: 5px #1d0f31 solid;
    border-radius: 50%;
    position: absolute;
    left: 50%;
    margin-top: 25px;
    margin-left: -15px;
}

a.bnt-more {
    background: #1C0F31;
    color: white;
    padding: 8px 20px;
    text-transform: uppercase;
    font-size: 14px;
    margin-top: 10px;
    margin-left: 20px;
    margin-bottom: 5px;
    display: inline-block;
    border-radius: 2px;
    box-shadow: 0 1px 3px -1px rgba(0, 0, 0, .6);
}
a.bnt-more:hover, a.bnt-more:active, a.bnt-more:focus {
    background: white;
    color: #1C0F31;
    text-decoration: none;
}

.timeline-card {
    padding: 0!important;
}
.timeline-content p {
    padding: 0 20px;
}


.timeline-img-header {
    height: 200px;
    position: relative;
    margin-bottom: 20px;
}

.timeline-img-header h2 {
    color: white;
    position: absolute;
    bottom: 5px;
    left: 20px;
}
.timeline-img-header.no-img {
    height: 100px;
}

blockquote {
    margin-top: 30px;
    color: grey;
    border-left-color: blue;
    padding: 0 20px;
}

.timeline-content .date {
    background: #1C0F31;
    display: inline-block;
    color: white;
    padding: 10px;
    position: absolute;
    top: 0;
    right: 0;
}

.timeline-bottom {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    padding-bottom: 15px;
}
.timeline-geo {
    display: flex;
    margin: 0px 20px 0px 20px;
    align-items: center;
}
.timeline-geo i.fa.fa-map-marker {
    font-size: 2rem;
    margin-right: 7px;
}
.geotooltip {
    border: none !important;
    cursor: zoom-in !important;
}
.geotooltip span {
    border-bottom: 1px dotted #000000;
    font-size: 0.9em;
}
@media (min-width: 1200px) {
    .geotooltip {
        max-width: 260px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
}


@media screen and (max-width: 768px) {

    .timeline-frame:before {
        left: 50px;
    }

    .timeline-img {
        left: 50px;
    }

    .timeline-content {
        max-width: 100%;
        width: auto;
        margin-left: 80px;
    }

    .timeline-item:nth-child(even) .timeline-content {
        float: none;    
    }

    .timeline-item:nth-child(odd) .timeline-content:after {
        content: '';
        position: absolute;
        border-style: solid;
        width: 0;
        height: 0;
        top: 30px;
        left: -15px;
        border-width: 10px 15px 10px 0;
        border-color: transparent #1C0F31 transparent transparent;
    }

}
```






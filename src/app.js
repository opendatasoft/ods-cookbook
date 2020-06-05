import './app.scss'

import initScroller from './plugins/scroll.js'

import colorCode from './components/codebox/index.js'
import { createList, revealItem } from './components/reveal-list/index.js'
import { initMapbox, zoomIn, zoomOut } from './components/mapbox/index.js'

/* If the value of a data-feature attribute is found here, it will use the
provided functions for enter, exit and progress events. Else it default to adding
the .active class to the div with matching id */
const scrollActions = {
  'reveal-list': {
    progress: revealItem
  },
  mapbox: {
    enter: zoomIn,
    exit: zoomOut
  }
}

initScroller(scrollActions)
colorCode()
createList()
initMapbox()

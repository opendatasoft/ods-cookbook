import scrollama from 'scrollama'

// default functions if you add nothing in the callbacks mapping
const addActiveClass = (response) => {
  const feature = document.getElementById(response.element.dataset.feature)
  feature.classList.add('active')
  response.element.classList.add('active')
}

const removeActiveClass = (response) => {
  const feature = document.getElementById(response.element.dataset.feature)
  feature.classList.remove('active')
  response.element.classList.remove('active')
}

export default (callbacks) => {
  const scroller = scrollama()

  //This a general setting that accepts any callback at enter and exit.
  // Most of the time you wil use only one function such as toggleActiveClass, in which case it's simpler to directly invoke the callback : 
  // scroller
  //   .setup({
  //     step: '.step',
  //     offset: 0.5,
  //     progress: true
  //   })
  //   .onStepEnter(toggleActiveClass)
  //   .onStepExit(toggleActiveClass)

  scroller
    .setup({
      step: '.step',
      offset: 0.5,
      progress: true
    })
    .onStepEnter((response) => {
      const stepCallbacks = callbacks[response.element.dataset.feature] || {}
      const callback = stepCallbacks.enter || addActiveClass // If you don't specify a call, it widd add .active class on
      callback(response)
    })
    .onStepExit((response) => {
      const stepCallbacks = callbacks[response.element.dataset.feature] || {}
      const callback = stepCallbacks.exit || removeActiveClass
      callback(response)
    })
    .onStepProgress((response) => {
      const stepCallbacks = callbacks[response.element.dataset.feature] || {}
      stepCallbacks.progress && stepCallbacks.progress(response)
    })

  window.addEventListener('resize', scroller.resize)
}

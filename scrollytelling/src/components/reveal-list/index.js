/* global fetch */

const baseUrl = 'https://data.opendatasoft.com/api/v2/catalog/datasets/amenagements-velo-en-ile-de-france%40datailedefrance/'
const query = 'aggregates?select=sum(longueur) as long_tot, count(*) as num_bikepath&group_by=nom_com&sort=-long_tot&limit=10'
const list = document.getElementById('top-cities-bikepath')

const addItemToList = (aggregation) => {
  list.insertAdjacentHTML('beforeend',
    `<li class="list-group-item">
      ${aggregation.nom_com} : ${aggregation.long_tot / 1000} km (${aggregation.num_bikepath} bike paths)
    </li>`
  )
}

const createList = (response) => {
  fetch(baseUrl + query)
    .then(response => response.json())
    .then(data => data.aggregations.forEach(addItemToList))
}

const revealItem = (response) => {
  const nextItemIdx = Math.floor(response.progress * 10)
  const nodes = [...list.children]
  nodes.forEach((node, i) => {
    i <= nextItemIdx
      ? node.classList.add('visible')
      : node.classList.remove('visible')
  })
}

export { createList, revealItem }

# What dataset do I need?
To install this app, you need :
* Your local data on COVID, at least with a date and a zipcode field. It may have other categories such as race, gender, age etc. If you can choose the data scheme, having the same as the national data is the easiest way.
* The national COVID data, publicly available here: https://public.opendatasoft.com/explore/dataset/coronavirus-covid-19-pandemic-usa-counties/table/?disjunctive.province_state&disjunctive.admin2&sort=date. You can either get it from the *public* (default in the app) domain of Opendatasoft or you can federate it to your own domain, refined for your state.
* The county geometrical shape sate, publicly available here: https://public.opendatasoft.com/explore/dataset/us-county-boundaries/table/. You can either get it from the *public* (default in the app) domain of Opendatasoft or you can federate it to your own domain, refined for your state.

The two things you mainly need to change are the context for the local data and the analysis described in the following section.

# Contexts usage
In the example local data (`city` in this example), will be refined for :
* Positive cases (`citypos`) and death (`citydied`). Depending on the available data, this may be only one context.
* Selected zipcodes in the table (`selectedpos` and `selecteddied`)

Based on your datascheme, these are the context you should change. But they should match the same pattern: number of confirmed cases and number of death, for each date, doubled to be refined by selected zipcode.

# Analysis explaination
Two main analysis are run both on positive cases and on number of deaths in this file :
* Sum of all records for each dates (x-axis), to get the last value and then the total as a subbaggregation.
* Sum of all record for each zipcodes (x-axis), for the maps and table.

Again, based on your available datascheme, the sum methodology will change but you should have : total for each day and total for all zipcodes, for both positive cases and deaths.

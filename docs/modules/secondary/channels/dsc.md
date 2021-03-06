
you specify the  model, module   and the model fields to be returned
you start from Dsc > Data List
here is where you set the data_name then in the query field is where you'll configure the module and model
and the fields
there are also more configurations you can do like joins, ordering depending on the data you want to query

on query 

the main fields are 

Module name: the module that has the module, this are the switch django apps 
must be in lowercase, the possible options are listed in 

Model name: a model in the module, has a corresponding database table created by django

# Columns returned

Values: the model fields, will be the database columns 
they are formatted in this way 

id%id|name%name

table_column_title1%model_field_path1|table_column_title2%model_field_path2


if we reference the many to many object fields, it will return a list for every item in the many to many field


## Filtering 

For q to filter, you need to add the fields to be filtered
If you need an AND filter, you use the and_filter field
If you need an OR filter, you use the or_filter field
If its a filter that has a list, list_filter would be used
Basically, the same query used on the header filters would be used with q

For and and or filters, you would require the alias%field|alias%field|alias%field
q would be filtering on fields All fields
The alias would be for direct particular field matching with its alias
Meaning, q would do all fields, and alias would do only its field

payload['q'] will filter all fields in AND and OR payload['alias'] will filter only the alias column

--


or_filters -> adds search input fields
e.g
service__name|gateway_profile__msisdn__phone_number


list_filters -> adds column dropdowns to datalist
this provides a means of filtering down for only a specific row column
e.g 
service__name|gateway_profile__msisdn__phone_number

### Advanced Filtering 
Advanced query filtering can be achieved using joins, 
i.e if you want to filter a model based on related entries on another model with no direct 
relation such as foreign key

real example

you have 2 models 
1. PostOffice with fields name and post_code 
2. GatewayProfile with fields postal_code
> Note PostOffice is a thirdparty module so fk won't work

say there are no keys relating the 2 models but post_code is the same as postal_code

Now to filter a PostOffice name for a given gateway profile from the profile's postal code
the query will be setup to Filter PostOffice names but then a join not query will be
needed to compare and filter out the PostOffice names that don't have the profile's code



the power of joins are useful at the fields part, there are 2 categories

1. Yes Fields -> filter rows where QueryModel.field == JoinModel.field
2. Not Fields -> filter only rows where QueryModel.field != JoinModel.field



## Action
added using *Data list link querys*
> the Link Name must be unique


## Indexing
used to specify the columns to return
format Column1|Column2|Column2|

## Response Format
supported response types
this is configurable in the datalist ... TODO

1 - LIST
this is a like a json table view,
there is a list of columns description then a list of rows for the columns

the columns describe the following about the row
- datatype
    date - a date with no time
    datetime - a date with a time
    > please note that the date is iso formated
    href - links/actions
- name -  the name of the column
- value - the queried database path
- list_filter 
- search_filter


2 - DATA
this  outputs the data formated as objects in the data 

3 - STRING


the response will also contain other data properties
page_count
page


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import time
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output,State,MATCH,ALL
import pandas as pd
import base64
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask
from dash.exceptions import PreventUpdate
from dash import dash_table
import charts
import os
import json
#import requests

'''
df1=pd.read_csv('summary.csv')
ov_pov_text = []
new_pov_text = []
pov_change_text = []
for ind in df1.index:
    ov_pov=df1['total_pov_rate'][ind]
    new_pov=df1['new_total_pov_rate'][ind]
    pov_change=df1['total_pov_change'][ind]

    ov_poverty=str( round(ov_pov*100,2)) +'%'
    new_poverty=str( round(new_pov*100,2)) +'%'
    poverty_change=str(pov_change)+'%'

    ov_pov_text.append(ov_poverty)
    new_pov_text.append(new_poverty)
    pov_change_text.append(poverty_change)

df1['total_pov_rate_%'] = ov_pov_text
df1['new_total_pov_rate_%'] = new_pov_text
df1['total_pov_change_%'] = pov_change_text
df1.to_csv('summary.csv',index=False)
'''




#from geojson_rewind import rewind



'''
with open('districts_.json', 'r') as openfile:
    # Reading from json file
    districts = json.load(openfile)

for k in range(len(districts['features'])):
    districts['features'][k]['properties'] = {'name':'{}'.format(k+1)}
    print(districts['features'][k]['properties'])



#print(len(districts['features']))
with open("districts_.json", "w") as outfile:
    json.dump(districts, outfile)
'''

'''
start=time.time()
response = requests.get('https://raw.githubusercontent.com/fedderw/maryland-child-allowance/master/data/external/Maryland_Election_Boundaries_-_Maryland_Legislative_Districts_2012.geojson')
print(time.time()-start)
cts=response.json()
print(cts["features"][0])
'''

'''
with urlopen('https://raw.githubusercontent.com/fedderw/maryland-child-allowance/master/data/external/Maryland_Election_Boundaries_-_Maryland_Legislative_Districts_2012.geojson') as response:
    print(response)
counties = json.load(response)

cts=counties["features"][0]
print(cts)
'''




#D1D3D4 grey
#f7f7f7 light grey
#fffbff off white
components_colors={ 'Color': ['Current', 'Default'], 'Main Background': ['white', 'white'],
             'Header Background': ['white', 'white'], 'Main Header Text': ['#E02A3E', '#E02A3E'],
             'Containers Background': ['#D1D3D4', '#D1D3D4'], 'Containers Label': ['black', 'black'],
             'Buttons': ['#E02A3E', '#E02A3E'], 'Buttons Text': ['white', 'white'],'Logo Text':['black','black'],
                    'Filters Label':['black','black']}

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
summary_csv = os.path.join(THIS_FOLDER, 'summary.csv')
district_all_100_csv = os.path.join(THIS_FOLDER, 'district_all_100.csv')
district_all_200_csv = os.path.join(THIS_FOLDER, 'district_all_200.csv')
district_young_100_csv = os.path.join(THIS_FOLDER, 'district_young_100.csv')
district_young_200_csv = os.path.join(THIS_FOLDER, 'district_young_200.csv')
county_all_100_csv = os.path.join(THIS_FOLDER, 'county_all_100.csv')
county_all_200_csv = os.path.join(THIS_FOLDER, 'county_all_200.csv')
county_young_100_csv = os.path.join(THIS_FOLDER, 'county_young_100.csv')
county_young_200_csv = os.path.join(THIS_FOLDER, 'county_young_200.csv')
logo_file=os.path.join(THIS_FOLDER, 'mca-logo.png')
counties_file=os.path.join(THIS_FOLDER, 'counties.json')
districts_file=os.path.join(THIS_FOLDER, 'districts_data.json')

server = Flask(__name__)

app = dash.Dash(
    __name__,server=server,
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0, shrink-to-fit=no'
        }
    ] ,
)
app.title='Maryland Child Benefit Dashboard'
app.config.suppress_callback_exceptions = True





header_text=html.Div('Maryland Child Benefit Dashboard',id='main_header_text',className='main-header',
                     style=dict(color='#9D2235',
                     fontWeight='bold',fontSize='',marginTop='',marginLeft='',width='100%',paddingTop='1vh',paddingBottom='',
                     display= 'flex', alignItems= 'center', justifyContent= 'center'))

sub_text=html.Div('A child allowance would send unconditional monthly checks to parents and legal guardians across the state. Parents would receive a check per child. For example, with a $100 monthly child allowance a mother of three would receive $300 monthly to help support her family.',
                               id='logo_text',className='sub-text',
                     style=dict(color=components_colors['Logo Text'][0],
                     fontWeight='',fontSize='',marginTop='',marginLeft='',
                     width='100%', paddingTop='0.5vh', paddingLeft='',paddingBottom='0.5vh' ,
                     display='flex', alignItems='center', justifyContent='center'
                                ))

table_text=html.Div('Counties with smaller populations may have larger margins of error due to smaller sample sizes in Census data.',
                               id='table_text',className='table-text',
                     style=dict(color=components_colors['Logo Text'][0],
                     fontWeight='',fontSize='',marginTop='',marginLeft='',
                     textAlign='center',paddingTop=''
                                ))

db_header_text=  dbc.Col([ header_text,sub_text] ,
        xs=dict(size=9,offset=0), sm=dict(size=9,offset=0),
        md=dict(size=8,offset=0), lg=dict(size=8,offset=0), xl=dict(size=8,offset=0))



encoded = base64.b64encode(open(logo_file, 'rb').read())
logo_img=html.Div( html.Img(src='data:image/jpg;base64,{}'.format(encoded.decode()), id='logo_img', height='',width='',className='mylogo'
                  )
                   ,style=dict(paddingTop='',paddingBottom='',))

db_logo_img=dbc.Col([ logo_img] ,
        xs=dict(size=3,offset=0), sm=dict(size=3,offset=0),
        md=dict(size=2,offset=0), lg=dict(size=2,offset=0), xl=dict(size=2,offset=0))


filters_header= html.Div(html.H1('Apply Filters',className= '', id='filters_header',
                                    style=dict(fontSize='', fontWeight='bold', color='#E02A3E',
                                               marginTop='')),
                            style=dict(display='', marginLeft='', textAlign="center", width='100%'))

age_text= html.Div(html.H1('Eligible Age Group',className= 'filters-header',id='age_text',
                                    style=dict(fontSize='', fontWeight='bold', color=components_colors['Filters Label'][0],
                                               marginTop='')),
                            style=dict(display='', marginLeft='', textAlign="left", width='100%'))
age_filter = html.Div(
    [
        dbc.RadioItems( options=[ {"label": "All Children (0 - 18)", "value": 'all'},
                                  {"label": "Young Children (0 - 4)", "value": 'young'},],
            value='all',
            id="age_filter",
            inline=False, label_class_name='filter-label',input_class_name='filter-button',input_checked_class_name='filter-button-checked' ,
            input_checked_style=dict(backgroundColor='#E02A3E',border='2px solid #E02A3E')
        ),
    ]
)

age_filter_div= html.Div([age_text , age_filter],
                            style=dict(fontSize='',display='inline-block',marginLeft='',textAlign="",marginBottom='',
                                       verticalAlign=''))

allowance_text= html.Div(html.H1('Child Allowance',className= 'filters-header',id='allowance_text',
                                    style=dict(fontSize='', fontWeight='bold', color=components_colors['Filters Label'][0],
                                               marginTop='')),
                            style=dict(display='', marginLeft='', textAlign="left", width='100%'))
allowance_filter = html.Div(
    [
        dbc.RadioItems( options=[ {"label": "$100 Monthly", "value": '100'},
                                  {"label": "$200 Monthly", "value": '200'},],
            value='200',
            id="allowance_filter",
            inline=False, label_class_name='filter-label',input_class_name='filter-button',input_checked_class_name='filter-button-checked' ,
            input_checked_style=dict(backgroundColor='#E02A3E',border='2px solid #E02A3E')
        ),
    ]
)

allowance_filter_div= html.Div([allowance_text , allowance_filter],
                            style=dict(fontSize='',display='inline-block',marginLeft='3vw',textAlign="",marginBottom='',
                                       verticalAlign=''))

location_text= html.Div(html.H1('Location',className= 'filters-header',id='location_text',
                                    style=dict(fontSize='', fontWeight='bold', color=components_colors['Filters Label'][0],
                                               marginTop='')),
                            style=dict(display='', marginLeft='', textAlign="left", width='100%'))
location_filter = html.Div(
    [
        dbc.RadioItems( options=[ {"label": "County", "value": 'county'},
                                  {"label": "State Districts", "value": 'districts'},],
            value='county',
            id="location_filter",
            inline=False, label_class_name='filter-label',input_class_name='filter-button',input_checked_class_name='filter-button-checked' ,
            input_checked_style=dict(backgroundColor='#E02A3E',border='2px solid #E02A3E')
        ),
    ]
)

location_filter_div= html.Div([location_text , location_filter],
                            style=dict(fontSize='',display='inline-block',marginLeft='3vw',textAlign="",marginBottom='',
                                       verticalAlign=''))

filters_button=html.Div([dbc.Button("Apply",size='lg',outline=False, color="primary", className="me-1", n_clicks=0,id="filters_button"
                            ,style=dict(fontWeight='bold',border='1px solid transparent',
                                        backgroundColor=components_colors['Buttons'][0],
                                        color=components_colors['Buttons Text'][0]
                                        )
                            )],style=dict(display='block',paddingTop='0.5vh'))


filters_buttons_div=html.Div([filters_button],
                                style=dict(width='100%',
                     display= 'flex', alignItems= 'center', justifyContent= 'center'))

filters_div=html.Div([age_filter_div,allowance_filter_div,location_filter_div],
                     style=dict(width='100%',paddingTop='1vh',paddingBottom='1vh',
                     display= 'flex', alignItems= 'center', justifyContent= 'center'))


#D1D3D4
'''
template={'data': {'indicator': [{
       'title': {'text': "inequality decreased by",'font':{'color':'black','family':'Arial'}},}]
   }}
   title='<b>inequality decreased by<b>',title_x=0.5,font=dict(color='black',size=13)
   '''
inequality_text= html.Div(html.H1('Child poverty decreased by',className= 'filters-header',id='inequality_text',
                                    style=dict(fontSize='', fontWeight='bold', color=components_colors['Filters Label'][0],
                                               marginTop='')),
                            style=dict(display='', marginLeft='', textAlign="center", width='100%'))


fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "delta",
    value = 100-34.4,
    delta = {'reference': 100, 'relative': True,'font': {'color': 'red', 'size': 30}},
   domain={'row':0,'column':0}
))

fig.update_layout(paper_bgcolor = "#EDEDED",plot_bgcolor='white',height=70,margin=dict(l=0, r=0, t=0, b=0),

                  )

inequality_indicator=html.Div(dcc.Graph(figure=fig,config={'displayModeBar': False},id='inequality_indicator',style=dict(width='100%')),className='num'
                              ,style=dict(width='100%'))



inequality_indicator_div=html.Div([inequality_indicator],style=dict(width='100%',
                     display= 'flex', alignItems= 'center', justifyContent= 'center'))




poverty_text= html.Div(html.H1('Total children lifted out of poverty',className= 'filters-header',id='poverty_text',
                                    style=dict(fontSize='', fontWeight='bold', color=components_colors['Filters Label'][0],
                                               marginTop='')),
                            style=dict(display='', marginLeft='', textAlign="center", width='100%'))

fig2 = go.Figure()

fig2.add_trace(go.Indicator(
    mode = "number",
    value = 55973,
    number={'font':{'color':'green','size':42},'valueformat':","},
   domain={'row':0,'column':0}
))

fig2.update_layout(paper_bgcolor = "#EDEDED",plot_bgcolor='white',height=70,margin=dict(l=0, r=0, t=0, b=0),

                  )

poverty_indicator=html.Div(dcc.Graph(figure=fig2,config={'displayModeBar': False},id='poverty_indicator',style=dict(width='100%')),className='num'
                           , style=dict(width='100%')  )



poverty_indicator_div=html.Div([poverty_indicator],style=dict(width='100%',
                     display= 'flex', alignItems= 'center', justifyContent= 'center'))




bar_fig_title= html.Div(html.H1('kids lifted out of poverty',className= 'bar-fig-header',id='bar_fig_title',
                                    style=dict(fontSize=18, fontWeight='bold', color=components_colors['Filters Label'][0],
                                               marginTop='')),
                            style=dict(display='', marginLeft='', textAlign="center", width='100%'))

bar_fig=go.Figure()
bar_div=html.Div([
            dcc.Graph(id='bar_chart', config={'displayModeBar': False},className='bar-fig',
                style=dict(height='',backgroundColor='#D1D3D4') ,figure=bar_fig
            ) ] ,id='bar_div'
        )

table = html.Div([dash_table.DataTable()], id='table_div')

#style_data_conditional = [{'if': {'filter_query': '{Simulated_Trips} != {Trips}', 'column_id': 'Simulated_Trips'},
 #                          'backgroundColor': 'skyblue'}]

map_header= html.Div(html.H1('New child poverty rate by county',className= 'filters-header',id='map_header',
                                    style=dict(fontSize='', fontWeight='bold', color=components_colors['Filters Label'][0],
                                               marginTop='')),
                            style=dict(display='', marginLeft='', textAlign="center", width='100%'))


map=go.Figure(px.choropleth())
map_div=html.Div([
            dcc.Graph(id='map_chart', config={'displayModeBar': True,'displaylogo': False,'modeBarButtonsToRemove': ['lasso2d','pan']},className='map-fig',
                style=dict(height='',backgroundColor='#f7f7f7',border='') ,figure=map
            ) ] ,id='map_div'
        )

main_layout=html.Div([dbc.Row([db_logo_img,db_header_text],
                              style=dict(backgroundColor=components_colors['Header Background'][0]),id='main_header' )
 #   ,html.Br()
    ,

       dbc.Row([

           dbc.Col([dbc.Card(dbc.CardBody([filters_div,filters_buttons_div])
        , style=dict(backgroundColor='#EDEDED'),id='card1',className='filters-card'), html.Br()
    ], xl=dict(size=6,offset=1),lg=dict(size=6,offset=1),
                     md=dict(size=6,offset=0),sm=dict(size=12,offset=0),xs=dict(size=12,offset=0)),

           dbc.Col([dbc.Card(dbc.CardBody([inequality_text,
                    dbc.Spinner([inequality_indicator],size="lg", color="danger", type="border", fullscreen=False,
                                spinner_style=dict(marginTop='8vh'))


                                           ])
                             , style=dict(backgroundColor='#EDEDED'), id='card2',
                             className='filters-card'), html.Br()
                    ], xl=dict(size=2, offset=0), lg=dict(size=2, offset=0),
                   md=dict(size=3, offset=0), sm=dict(size=6, offset=0), xs=dict(size=6, offset=0)),

           dbc.Col([dbc.Card(dbc.CardBody([poverty_text,
                    dbc.Spinner([poverty_indicator],size="lg", color="danger", type="border", fullscreen=False,
                                spinner_style=dict(marginTop='8vh'))

                                           ])
                             , style=dict(backgroundColor='#EDEDED'), id='card3',
                             className='filters-card'), html.Br()
                    ], xl=dict(size=2, offset=0), lg=dict(size=2, offset=0),
                   md=dict(size=3, offset=0), sm=dict(size=6, offset=0), xs=dict(size=6, offset=0)),

           dbc.Col([dbc.Card(dbc.CardBody(
               [ map_header,dbc.Spinner([map_div], size="lg", color="danger", type="border", fullscreen=False)

                ])
                             , style=dict(backgroundColor='#f7f7f7'), id='card4',
                             className='charts-card'), html.Br()
                    ], xl=dict(size=6, offset=1), lg=dict(size=6, offset=1),
                   md=dict(size=6, offset=0), sm=dict(size=12, offset=0), xs=dict(size=12, offset=0)),



           dbc.Col([dbc.Card(dbc.CardBody([html.Br(),dbc.Spinner([bar_div],size="lg", color="danger", type="border", fullscreen=False )

                                           ])
                             , style=dict(backgroundColor='#f7f7f7'), id='card5',
                             className='charts-card'), html.Br()
                    ], xl=dict(size=4, offset=0), lg=dict(size=4, offset=0),
                   md=dict(size=6, offset=0), sm=dict(size=12, offset=0), xs=dict(size=12, offset=0))


]),
                   html.Br(),

                      dbc.Row([dbc.Col([dbc.Spinner([table],size="lg", color="danger", type="border", fullscreen=False,
                                                    spinner_style=dict(marginTop='8vh'))]
                    , xl=dict(size=10, offset=1), lg=dict(size=10, offset=1),
                   md=dict(size=12, offset=0), sm=dict(size=12, offset=0), xs=dict(size=12, offset=0))

                      ]) , table_text

])



app.layout = html.Div([main_layout,html.Br(),html.Br()

                       ], style=dict(backgroundColor=components_colors['Main Background'][0]), className='main',
                      id='main_div')

# age_filter all young  allowance_filter 100 200
'''
If all kids and $100 then box 1 is 20.4% and box 2 is 35,049
If all kids and $200 then box 1 is 34.4% and box 2 is 55,973
If young kids and $100 then box 1 is 4.3% and box 2 is 7,672
If young kids and $200 then box 1 is 8.1% and box 2 is 13,949

'''
# inequality_indicator poverty_indicator
@app.callback([Output('bar_chart','figure'),Output('inequality_indicator','figure'),Output('poverty_indicator','figure')],
              Input('filters_button','n_clicks'),
              [State('age_filter','value'),State('allowance_filter','value')]
              )
def update_figures(clicks,age,allowance):
    summary = pd.read_csv(summary_csv)
    df=pd.DataFrame()
    pov_dec=34.4
    pov_out = 55973

    if age=='all' and allowance=='100':
        df=summary[summary['reform'] == 'All Children 100']
        pov_dec=20.4
        pov_out=35049
    elif age=='all' and allowance=='200':
        df=summary[summary['reform'] == 'All Children 200']
        pov_dec=34.4
        pov_out=55973
    elif age=='young' and allowance=='100':
        df=summary[summary['reform'] == 'Young Children 100']
        pov_dec=4.3
        pov_out=7672
    elif age=='young' and allowance=='200':
        df=summary[summary['reform'] == 'Young Children 200']
        pov_dec=8.1
        pov_out=13949

    my_bar_fig=charts.create_bar_chart(df)
    box1 = go.Figure()

    box1.add_trace(go.Indicator(
        mode="delta",
        value=100 - pov_dec,
        delta={'reference': 100, 'relative': True, 'font': {'color': 'red', 'size': 30}},
        domain={'row': 0, 'column': 0}
    ))

    box1.update_layout(paper_bgcolor="#EDEDED", plot_bgcolor='white', height=70,
                      margin=dict(l=0, r=0, t=0, b=0),

                      )

    box2 = go.Figure()

    box2.add_trace(go.Indicator(
        mode="number",
        value=pov_out,
        number={'font': {'color': 'green', 'size': 42}, 'valueformat': ","},
        domain={'row': 0, 'column': 0}
    ))

    box2.update_layout(paper_bgcolor="#EDEDED", plot_bgcolor='white', height=70,
                       margin=dict(l=0, r=0, t=0, b=0),

                       )

    return (my_bar_fig,box1,box2)

# location_filter county districts
@app.callback(Output('table_div','children'),
              Input('filters_button','n_clicks'),
              [State('age_filter','value'),State('allowance_filter','value'),State('location_filter','value')]
              )
def update_table(clicks,age,allowance,location):
    df=pd.DataFrame()
    if age=='all' and allowance=='100' and location=='county':
        df=pd.read_csv(county_all_100_csv)
        maryland_df = df[df['County'] == 'Maryland']
        df.drop(maryland_df.index, inplace=True)
        df.reset_index(drop=True,inplace=True)
        df=pd.concat([maryland_df, df], ignore_index=True)

    elif age=='all' and allowance=='200' and location=='county':
        df=pd.read_csv(county_all_200_csv)
        maryland_df = df[df['County'] == 'Maryland']
        df.drop(maryland_df.index, inplace=True)
        df.reset_index(drop=True,inplace=True)
        df=pd.concat([maryland_df, df], ignore_index=True)

    elif age=='young' and allowance=='100' and location=='county':
        df=pd.read_csv(county_young_100_csv)
        maryland_df = df[df['County'] == 'Maryland']
        df.drop(maryland_df.index, inplace=True)
        df.reset_index(drop=True,inplace=True)
        df=pd.concat([maryland_df, df], ignore_index=True)

    elif age=='young' and allowance=='200' and location=='county':
        df=pd.read_csv(county_young_200_csv)
        maryland_df = df[df['County'] == 'Maryland']
        df.drop(maryland_df.index, inplace=True)
        df.reset_index(drop=True,inplace=True)
        df=pd.concat([maryland_df, df], ignore_index=True)

    elif age=='all' and allowance=='100' and location=='districts':
        df=pd.read_csv(district_all_100_csv)

    elif age=='all' and allowance=='200' and location=='districts':
        df=pd.read_csv(district_all_200_csv)

    elif age=='young' and allowance=='100' and location=='districts':
        df=pd.read_csv(district_young_100_csv)

    elif age=='young' and allowance=='200' and location=='districts':
        df=pd.read_csv(district_young_200_csv)

    mytable=dash_table.DataTable(
        columns=[
            {
                'name': str(x), 'id': str(x), 'deletable': False,
            } for x in df.columns
        ], id='table', page_size=13, data=df.to_dict('records')
        , style_cell=dict(textAlign='center', border='2px solid black'
                          , backgroundColor='white', color='black', fontSize='1.8vh', fontWeight=''),
        style_header=dict(backgroundColor='#D9D9D9', color='black',
                          fontWeight='bold', border='2px solid black', fontSize='1.8vh'),
        editable=False, row_deletable=False, sort_action="native",
        sort_mode="single", page_action='native', style_table={'overflowX': 'auto','width':'100%','min-width':'100%'},

         fixed_columns=dict(headers=True,data=1)
        # it was here

        # 'overflowY': 'auto',
    )

    return mytable


@app.callback([Output('map_chart','figure'),Output('map_header','children')],
              Input('filters_button','n_clicks'),
              [State('age_filter','value'),State('allowance_filter','value'),State('location_filter','value')]
              )
def update_map(clicks,age,allowance,location):
    map_df = pd.DataFrame()
    if age == 'all' and allowance == '100' and location == 'county':
        map_df = pd.read_csv(county_all_100_csv)



    elif age == 'all' and allowance == '200' and location == 'county':
        map_df = pd.read_csv(county_all_200_csv)



    elif age == 'young' and allowance == '100' and location == 'county':
        map_df = pd.read_csv(county_young_100_csv)



    elif age == 'young' and allowance == '200' and location == 'county':
        map_df = pd.read_csv(county_young_200_csv)



    elif age == 'all' and allowance == '100' and location == 'districts':
        map_df = pd.read_csv(district_all_100_csv)

    elif age == 'all' and allowance == '200' and location == 'districts':
        map_df = pd.read_csv(district_all_200_csv)

    elif age == 'young' and allowance == '100' and location == 'districts':
        map_df = pd.read_csv(district_young_100_csv)

    elif age == 'young' and allowance == '200' and location == 'districts':
        map_df = pd.read_csv(district_young_200_csv)

    if location =='county':

        with open(counties_file, 'r') as openfile:
            counties = json.load(openfile)

        map_df['N Reform child poverty rate'] = map_df['Reform child poverty rate'].apply(lambda x: float(x[0:-1]))

        '''
        map_df['N Original overall poverty rate'] = map_df['Original overall poverty rate'].apply(
            lambda x: float(x[0:-1]))
        map_df['N Reform overall poverty rate'] = map_df['Reform overall poverty rate'].apply(lambda x: float(x[0:-1]))
        original = map_df['N Original overall poverty rate']
        new = map_df['N Reform overall poverty rate']
        map_df['Percentage of poverty decreased'] = ((original - new) / original) * 100
        map_df['Percentage of poverty decreased'] = map_df['Percentage of poverty decreased'].round(2)
        map_df['Percentage of poverty decreased'] = map_df['Percentage of poverty decreased'].apply(
            lambda x: str(x) + '%')

        poverty_ranges = [0, 10, 20, 100]
        poverty_labels = ['0-10%', '10-20%', '20-100%']
        map_df['Poverty_Ranges'] = pd.cut(map_df['N Original overall poverty rate'], bins=poverty_ranges,
                                          labels=poverty_labels)
        '''

        map_fig = px.choropleth(map_df, geojson=counties, locations='County', color='N Reform child poverty rate',
                                color_continuous_scale="Reds",
                        #        range_color=[0,100],

                                    labels={'Original child poverty rate': '<b>Original child poverty rate<b>',
                                        'County': '<b>County<b>',
                                        "Reform child poverty rate": "<b>New child poverty rate<b>",
                                        'Change in child poverty': '<b>Change in child poverty rate<b>'},

                                featureidkey="properties.name",
                                hover_data={"Original child poverty rate": True, "Reform child poverty rate": True,
                                            'N Reform child poverty rate': False,
                                            'Change in child poverty': True}
                                )
        map_fig.update_layout(margin=dict(l=0, r=0, t=0, b=0),
                              mapbox=dict(style='basic'),
                              coloraxis=dict(showscale=False,
                                             colorbar=dict(len=0.7, yanchor='middle', y=0, thickness=20, x=0.5,
                                                           ticklen=3, orientation='h',
                                                           title=dict(font=dict(size=16, color='black'), side='top',
                                                                      text='<b>% of Poverty<b>')
                                                           )),
                              plot_bgcolor='#f7f7f7', paper_bgcolor='#f7f7f7', legend=dict(yanchor="bottom", y=0.5),
                              # ,height=700,width=1100
                              )
        map_fig.update_geos(fitbounds="locations", visible=False, bgcolor='#f7f7f7',projection=dict(type='boggs'))
        counties=None
        return ( map_fig ,'New child poverty rate by county')

    elif location=='districts':
        with open(districts_file, 'r') as openfile:
            # Reading from json file
            districts = json.load(openfile)

        # districts=rewind(districts,rfc7946=False)


        #map_df['District'] = map_df['District'].apply(lambda x: x.replace('0', ''))

        map_df['N Reform child poverty rate'] = map_df['Reform child poverty rate'].apply(lambda x: float(x[0:-1]))

        map_fig = px.choropleth(map_df, geojson=districts, locations='District', color='N child overall poverty rate',
                             color_continuous_scale="Reds", featureidkey="properties.name",
                                labels={'Original child poverty rate': '<b>Original child poverty rate<b>',
                                        'District': '<b>District<b>',
                                        "Reform child poverty rate": "<b>New child poverty rate<b>",
                                        'Change in child poverty': '<b>Change in child poverty<b>'},

                                hover_data={"Original child poverty rate": True, "Reform child poverty rate": True,
                                            'N Reform child poverty rate': False,
                                            'Change in child poverty': True}
                             )

        map_fig.update_layout(margin=dict(l=0, r=0, t=0, b=0),
                              mapbox=dict(style='basic'),
                              coloraxis=dict(showscale=False,
                                             colorbar=dict(len=0.7, yanchor='middle', y=0, thickness=20, x=0.5,
                                                           ticklen=3, orientation='h',
                                                           title=dict(font=dict(size=16, color='black'), side='top',
                                                                      text='<b>% of Poverty<b>')
                                                           )),
                              plot_bgcolor='#f7f7f7', paper_bgcolor='#f7f7f7', legend=dict(yanchor="bottom", y=0.5),
                              # ,height=700,width=1100
                              )
        map_fig.update_geos(fitbounds="locations", visible=False, bgcolor='#f7f7f7',projection=dict(type='boggs'))

        districts = None
        return (map_fig,'New child poverty rate by district')
if __name__ == '__main__':
    app.run_server(host='localhost',port=8055,debug=False,dev_tools_silence_routes_logging=True)
import plotly.express as px

def create_bar_chart(dataframe):
  df = dataframe

  fig = px.bar(df, x="age_group", y="total_pov_change",
              labels={
                     "total_pov_change_%": "<b>Change in child poverty rate<b>",
                     "total_pov_rate_%": "<b>Original child poverty rate<b>",
                     "new_total_pov_rate_%": "<b>New child poverty rate<b>",
                    'age_group':'<b>Age Group<b>', 'total_pov_change':'<b>Change in the SPM poverty rate<b>'
                 }
               ,
               hover_data={'total_pov_rate_%':True,'new_total_pov_rate_%':True,'total_pov_change_%':True,
                           'age_group':False,'total_pov_change':False}
               ,
             #   title="<b>Change in child poverty by age group<b>",
             color='age_group',
             text='total_pov_change',
             color_discrete_map={
                                 'All': '#003f5c',
                                 'Adult': '#5886a5',
                                 'Child': '#5886a5',
                                 'Young Child': '#5886a5'})

  fig.update_layout(showlegend=False, yaxis_ticksuffix='%',plot_bgcolor='#f7f7f7',
                    paper_bgcolor='#f7f7f7' ,margin=dict(l=0, r=0, t=0, b=0),
                    title_x=0.5,font=dict(color='black',size=12))
  fig.update_traces(texttemplate='%{text}%')
  fig.update_xaxes(showgrid=False, showline=True, zeroline=False,linecolor='black')
  fig.update_yaxes(showgrid=False, showline=True, zeroline=False,linecolor='black')
  return fig
#D1D3D4 grey
#f7f7f7 light grey
#fffbff off white
'''










        sub_text=html.Div('A child allowance would send unconditional monthly checks to parents and legal guardians across the state. Parents would receive a check per child. For example, with a $100 monthly child allowance a mother of three would receive $300 monthly to help support her family.',
                     style=dict(color=components_colors['Logo Text'][0],position=''

                                ))

header_text=html.Div(['Maryland Child Benefit Dashboard'],id='main_header_text',className='main-header',
                     style=dict(color=components_colors['Main Header Text'][0],
                     fontWeight='bold',fontSize='',marginTop='',marginLeft='',width='',paddingTop='1vh',paddingBottom='',
                      alignItems= '', justifyContent= '',verticalAlign=''))

header_and_sub=html.Div([header_text,sub_text],style=dict(display= 'inline-block'))



encoded = base64.b64encode(open('mca-logo.png', 'rb').read())
logo_img=html.Div( html.Img(src='data:image/jpg;base64,{}'.format(encoded.decode()), id='logo_img', height='',width='',className='mylogo'
                  )
                   ,style=dict(paddingTop='',paddingBottom='',display='inline-block'))

    '''

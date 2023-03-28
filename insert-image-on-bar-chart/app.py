# import library
import os
import base64
from plotly import graph_objects as go


# preparing data
y_data = ['Euro','Serie A','La Liga',
        'Premier League','Champions League']
x_data = [1, 2, 2, 3, 5]

# create Bar Chart
fig = go.Figure(
            data=[go.Bar(
                y=y_data,
                x=x_data,
                width=0.6,                    
                text=[str(x)+" "+y for x,y \
                        in zip(x_data,y_data)],
                textfont=dict(color='#e6e8eb'),
                orientation='h',
                marker=dict(
                    color=[ '#6fa6f7']*5,
                ))
            ]
    )

layout=dict(
    title = dict(
        text='CR7 Has Conquered 5 Champions League & <br>7 European League Trophies In 3 Different Contries',
        font=dict(size=18,color="#585858"),
        pad=dict(l=-30)
                ),

    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        range=[0,9],autorange=False
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        range=[-1,6],autorange=False

    ),
    paper_bgcolor='rgba(255,255,255,0)',
    plot_bgcolor='rgba(255,255,255,0)',
    showlegend=False,
    font=dict(
        family="Arial",
        size=13,
        color="#585858"

    ),
    width=600,
    height=370,
    margin=dict(
        l=0,
        r=0,
        b=10,
        t=40,
        pad=10
    ),
)

annotations = [dict(x=0, y=5.5,
        text=f"Source : goal.com | freeiconspng.com",
        showarrow=False,
        xanchor='left',            
        font=dict(
            color='#909090',
            size=9
            ),
        ),]

# Get PNG filename
image_filename = os.getcwd()+os.sep+"assets"+os.sep+\
"cristiano-ronaldo-png-45111.png"
# Encode PNG Image to Base64
base64_string = base64.b64encode(
                open(image_filename, 'rb').read())
# Decode base64 string to PNG base64
base_64_png = base64_string.decode()

# Adding Images
images= [dict(
        source='data:image/png;base64,{}'.\
                format(base_64_png),
        xref="paper", yref="paper",
        xanchor="left",
        x=0.6, y=0.85,
        sizex=0.8, sizey=0.8,
        opacity=0.5,
        layer="below")]

fig.update_layout(layout,
        annotations = annotations,
        images=images
)

# Showing Bar chart
fig.show()


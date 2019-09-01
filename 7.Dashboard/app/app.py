import dash
import dash_core_components as dcc
import dash_html_components as html
import os
from callbacks import app_callbacks
from dash.dependencies import Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def create_app():
    app = dash.Dash()
    app.title = 'Restaurant Hygiene Prediction Dashboard'
    # app.config.supress_callback_exceptions=True
    return app

def init_layout():
    return html.Div([
        html.Meta(charSet='utf-8'),
        html.Meta(name='viewport',
                  content='width=device-width, \
                           initial-scale=1,\
                           shrink-to-fit=no'),
        html.H1(children='Restaurant Hygiene Predictions'),

        html.Div(children='''
            Enter restaurant reviews(if there are multiple reviews then seperate them with space)
        '''),
        dcc.Textarea(
            placeholder='Enter a value...',
            style={'width': '50%'},
            id= 'doc',
            value = 'I live up the street from Betty. &#160;When my sister was in town for Spring Break, we made an effort to hit several little places we had never been to before.BETTY WAS PRETTY SWEET!The service was lively. &#160;We made a reservation (via Yelp of course) and were seated right away by the window for a group of four. &#160;I love sitting by the window because I want to be seen when I\'m out. &#160;It was really a pleasant evening.Three of us had the Betty Burger, which was substantially larger than I expected. &#160;My sister had the pan roasted chicken, which was also generously portioned.For those of you who would be traveling to Queen Anne from elsewhere, FREE PARKING ON QUEEN ANNE AVE, WHOOOHOOO! :) Wow.. Came here for Happy Hour and never knew this place had a back room. I highly recommend coming here for Happy Hour. The place is classy with just enough dark ambiance to make this place sexy. The food was great! We went small place style and got the following items. Happy Hour Clams were amazing. The broth was interesting with just enough kick to it. Hour Hour Frites - Yummy fries. How can you go wrong with frieds.Happy Hour Lemon Drop - Tasty, tasty, tasty!Happy Hour Oysters - YUM!Happy Hour Wine by the glassMix GreenYes.. Betty. I heart you! I recently tried Betty for the first time and boy, am I ever a fan. The ambiance was fantastic. We were slightly surprised at how short the menu was. At first it put us off a little bit, but we both found something that sounded like it could be ok.When the food came, our choices were validated. I had the lamb ragout. It had plenty of meat, fresh peas, rich sauce and freshly made noodles. It was a huge amount of food but the flavors were so amazing that I managed to eat the entire thing.Be sure to get reservations (http://opentable.com makes it easy.) Not bad BettyWent here for dinner with friends. Don\'t be confused by the velvet curtain as you walk through the door. Weird way to keep the cold out. They can seat about 8 at most. The server was friendly. Tried the Betty burger and beer. Burger was huge and not as flavorful as I hoped. The fries were burnt and not that great. I tried my friend\'s dishes and I\'ll have to get the chicken next time. No one tried the rib eye steak and frites and I\'m curious about that one. The menu is already changing, but never let\'s me down. I\'ve been here at least 10 times and have never been served a mediocre meal --everything here is delicious.The service is exceptional and very friendly. The setting is casual, and conveniently located on Queen Anne Ave.It can be a little pricey, but certainly worth it. I wouldn\'t say that I was a fan, but this is an okay place to go. &#160;I\'d say it\'s a seven of ten more than a three of five, but I round halves down.Mom was up visiting from Alabama. &#160;I don\'t know why she ever agrees to go out with us, because it is always the same: &#160;too slow, too expensive, too salty, one dollar should be enough tip.This time she didn\'t grouse about the tip, although she\'d been skipped on the water service (as I had), but she remarked on the friendliness of the people there. &#160;Service was timely. &#160;I also ordered a to-go meal for my wife who wasn\'t with us, they timed it perfectly. &#160;On a separate check, in fact, which they had no problem doing.They got us in during Seattle Restaurant Week, which was awesome.I had the Wild Boar spaghetti (I think they had a fancier name for it, but that\'s what it was), which my brother also had. &#160;He didn\'t like it at first, but liked it at the end. &#160;I noticed no improvement, but I liked it from the get-go. &#160;Brother had a point though, he would have had no problem making any of those dishes at home, except the scrumptious desserts.The food was oversalted. &#160;The salt was pretty pervasive, and that\'s really my only knock on the joint.Takeaway: &#160;I recommend that you try it. &#160;I can see why some people have it as a favorite, it\'s just not one of mine. The only reason I wouldn\'t go back here is because your clothing always smells like bacon grease or something when you leave. &#160;It takes a few washes to get the smell out. &#160;Other than that, the wine pours are nice, the staff is great and their tapas is delish. &#160;Wear an old coat when you go there though, you\'ve been forewarned. This is my go-to restaurant for happy hour in Queen Anne! The menu is amazingly delicous, both for HH and the regular menu. The HH menu is priced really well and the five dollar wine pours are too tempting to not pass up! The frites are delicious with just the right amount of salt. They always have either clams or mussels, and both are my favorite thing to get off of the HH menu! The pulled pork mole tacos are tasty, too, and my husband always orders them when we go.Service is friendly, helpful and relaxed. They aim at letting you have a great time in the restarant, with no pressure about getting you in and out quickly, which is appreciated.Oh - and about two years ago I got a savory stinging nettle risotto that I still dream about to this day. It was THAT good. And right now I\'m waiting for the right time to go and have their halibut... oh it should be heavenly!Definitely go to Betty if you\'re around the top of QA. And by \'definitely go\', I mean, \'go all the time!\'PS: In the summertime they open up their back patio - woohoo!! Sunshine AND great food!! (Excellent time to get the prosecco and some salami + olives on a Friday evening!) The original dinner plan was Lloyd Martin, then suddenly the place was on fire. And by that I mean it included fire trucks. So, I met Peter and Ron at Betty instead. NEVER have I waited so long for a burger. The servers were incredibly good but the kitchen was as devastatingly slow as drowning in ice water in Hell. The drinks were weak and overly expensive.The food was average but sorta pretty.I rank Betty high for service only. My boyfriend and I were looking for a casual place to eat in Upper Queen Anne and have always wanted to try Betty. &#160;I was very surprised to see bottles of wine in ice buckets on customer\'s tables, but I was very pleased to see that we were in for a treat. &#160;We shared an order of Sauteed Squid and Green Olives, which was absolutely delicious as a starter. &#160;It was also pretty plentiful for an app. &#160;We both then shared a Ribeye Steak and also substituted the fries (after seeing a HEAPING load of fries on another customer\'s plate) with some mixed organic greens (yum!!). &#160;The ribeye steak was very plentiful, it would\'ve been too much for one person. &#160;It was SO GOOD. are you too lazy to marinate a chicken and pan roast it to perfection in a cast iron skillet for dinner tonight?not to worry, betty has got you covered. the meat will be succulent and well seasoned. heck, they will even through in some roasted potatoes and vegetables. who needs to order sides?i\'m afraid I won\'t order anything else here now. Found this place when our first choice in Queen Anne couldn\'t guarantee our reservation. Overall, we were quite pleased with the food and the ambience. Unlike some places nearby, you can actually have a conversation and it has a nice feel to it. &#160;The food is good,although the wine list leaves a bit to be desired.Service is OK. They are pleasant, but you get a lot of "no"\'s from them. Simple requests are greeted with a "no". &#160;We had a birthday, and while I really don\'t mind paying for my own dessert, an acknowledgement would at least be nice. &#160;Why else would you ask? This is a place that does things right. We went to Betty\'s for happy hour after walking y it so many times. All items were very reasonably priced, we tried several different things and we were pleased with all of them. The menu might be a bit too traditional if you will, but the food was cooked right. Also if you sit at the counter you can see the chefs cook your food which is a definite plus, I like to see what goes into my plate and I like it when the kitchen is kept in a proper manner and they are not afraid of showing it to the customers. Could be the nicest staff I\'ve ever encountered. &#160;And the food was excellent. &#160;I\'ll be back... Pretty good if you are looking for pub/bistro fare. But don\'t expect great things if you order a steak or anything "fancy." Delicious. Tthere are so many tempting things on their menu it\'s hard to know where to begin. &#160;The parmesan tarte is like a cloud--not quiche, not custard with the flavor of fresh parmesan, it defies words. &#160;The homemade pea soup equally fine--tasted the fresh herbs and split peas soft but still holding their shape, and not too heavily flavored with ham--perfect for this extended winter weather. &#160;Several entrees on the menu--fragrant chicken, a vegetarian tangine among others. I ordered the braised/stewed lamb shank. &#160;Betty\'s version is superb--marvelous lamb that has been slow cooked so that the meat falls off the bone served with a rich vegetable-enhanced tomato-based sauce and a bed of creamy polenta. &#160;Never had lamb that tasted as good as this. &#160;Usually declining dessert, on the fabulous $30 deal this month I indulged. Either of the homemade ice creams are sublime--one with a Guiness caramel sauce and the other, a homemade wedge of Neopolitan ice cream (the strawberry layer tasted like FRESH strawberries!) rests in a shallow pool of dark chocolate fudge sauce. &#160;And three thin dark chocolate shortbread coins hail invitingly from the top of the ice cream wedge daring you to dip them into the fudge sauce too! &#160;Strongly recommend Betty for anyone who knows the difference between ordinarily good and extraordinary! &#160;Betty is in that extra-excellent category. &#160; I found service to be wonderful--fast, warm, not intrusive and I liked the modern feel of the place. &#160;Lighting that was just right for regular meal or romance! Not pretentious, very welcoming, elegant enough to feel like you have dined well. This has become our "go-to" place for great food. &#160;It gets better every time we go. &#160;The burger is great, the chicken is great, and the cassoulet was amazing when we went. &#160;You can\'t go wrong with anything on the menu - check it out! The menu is small and simple and the atmosphere is exactly what you\'d expect in upper Queen Anne, a great date night spot. &#160;We were a little confused by the entrance which appears to be an entrance to nowhere, but once we passed through the curtain and took our seats everything was great. &#160;We both ended up with the roast chicken, partly because of an ordering gaffe on my part, but I couldn\'t have been happier. &#160;The chicken was moist and tender and had a delicious crispy skin and the portion size was perfect. &#160;Betty definitely found a spot in the regular rotation for me and the girlfriend. Never been here before or heard of the place. &#160;Went here for the $30 prix fixe menu..this was really a great neighborhood restaurant. &#160;Service was very very slow though...first course was parmesan pudding and grapefruit vinigrette...$12 and $14 respectively...very tasty, the grapefruit added a nice kick..the melted parmesan on crostini was very tasty and it had a pesto add in to round it off...entree was roast chicken and pork loin atop savoy cabbage..the pork was really good and the sauce with the cabbage was very peppery...almost too peppery but I like spicy...The roast chicken was really good too, the breast was moist. &#160;mid $20 range for both..dessert was $8 for any dessert, got the guiness ice cream with brownie bites without the shot of alcohol and the panna cotta...never had panna cotta before, it was with grapefruit....unusual gelatin consistency..not bad but not really good, the candied grapefruit rind was too intense...the ice cream was fine, just ice cream with brownies...can\'t go wrong with that... Don\'t think you can go wrong with Betty. Unpretentious, good food and service. Happy hour is especially nice, impressed with their wine by the glass selections and generous pours! Very comfortable, from making reservations the day of for a business dinner , to greeting us, to the ease of the menu. &#160; the Queen Anne area is a very busy place and parking is crazy. I had the duck confit with a lamb sausage, swiss chard. &#160;good comfort food for a california person eating in the "cold (not yet) NorthWest.'

        ),
        html.Div(children='''
            Enter average ratings
        '''),
        dcc.Input(
            placeholder='Enter a average rating...',
            type='number',
            id = 'average_ratings',
            value='4'
        ) ,
        html.Div(children='''
            Enter total reviews
        '''),
        dcc.Input(
            placeholder='Enter total reviews...',
            type='number',
            id = 'total_reviews',
            value='10'
        ) ,
        # html.Div(children='''
        #     Enter zipcode
        # '''),
        # dcc.Input(
        #     placeholder='Enter a zipcode...',
        #     type='number',
        #     id = 'zipcode',
        #     value='07003'
        # ) ,
        html.Div(children='''
            Choose restuarant cuisine
        '''),
        #replace this is dynamic callback that reads classes from MultiLabelBinarizer
        dcc.Dropdown(
            options=[
                {'label': i, 'value': i} for i in ['Afghan', 'African', 'American (New)', 'American (Traditional)',
               'Asian Fusion', 'Australian', 'Barbeque', 'Basque', 'Belgian',
               'Brazilian', 'Breakfast & Brunch', 'British', 'Buffets', 'Burgers',
               'Cafes', 'Cajun/Creole', 'Cambodian', 'Cantonese', 'Caribbean',
               'Cheesesteaks', 'Chicken Wings', 'Chinese', 'Colombian',
               'Comfort Food', 'Creperies', 'Cuban', 'Delis', 'Dim Sum', 'Diners',
               'Egyptian', 'Ethiopian', 'Fast Food', 'Filipino', 'Fish & Chips',
               'Fondue', 'Food Court', 'Food Stands', 'French', 'Gastropubs',
               'German', 'Gluten-Free', 'Greek', 'Haitian', 'Halal', 'Hawaiian',
               'Himalayan/Nepalese', 'Hot Dogs', 'Hot Pot', 'Indian',
               'Indonesian', 'Irish', 'Italian', 'Japanese', 'Korean', 'Kosher',
               'Laotian', 'Latin American', 'Lebanese', 'Live/Raw Food',
               'Malaysian', 'Mediterranean', 'Mexican', 'Middle Eastern',
               'Modern European', 'Mongolian', 'Moroccan', 'Pakistani',
               'Persian/Iranian', 'Pizza', 'Polish', 'Puerto Rican',
               'Restaurants', 'Russian', 'Salad', 'Salvadoran', 'Sandwiches',
               'Scandinavian', 'Scottish', 'Seafood', 'Senegalese',
               'Shanghainese', 'Soul Food', 'Soup', 'Southern', 'Spanish',
               'Steakhouses', 'Sushi Bars', 'Szechuan', 'Taiwanese', 'Tapas Bars',
               'Tapas/Small Plates', 'Tex-Mex', 'Thai', 'Trinidadian', 'Turkish',
               'Vegan', 'Vegetarian', 'Venezuelan', 'Vietnamese']
            ],
            style={'width': '70%'},
            multi=True,
            id = "cuisine",
            value=["Delis"]
        ),
        html.Button(id='submit-button', n_clicks=0, children='Submit'),
        html.Div(id='output-state')



    ])

# def create_callbacks(app, dev_mode):
#
#     app = individual_view_callbacks(app, undiagnosed_dfs, patient_output_dicts)
#     app = population_view_callbacks(app, diseases, short_disease_descriptions, undiagnosed_dfs, clfs,clf_probss, model_dfs, cf_dfs, patient_output_dicts)
#     return app


#Place here dynamic dropdown for cuisine types
# @app.callback(Output('shap-plot-wrap', 'children'),[], [State('input', 'value'), State('selected_disease', 'value')], [Event('button', 'click')])
# def update_table(selected_patient, selected_disease):
#     return [html.Div([html.Div(['Top Positive and Negative Influencers'],className='shap-text')],className='shap-text-wrapper'),shap_graph]



if __name__ == '__main__':
    app = create_app()

    app.layout = init_layout()
    app = app_callbacks(app)

    # @app.callback(Output('output-state', 'children'),
    #           [Input('submit-button', 'n_clicks')])
    # def update_output(n_clicks):
    #     return u'''
    #         The Button has been pressed {} times
    #     '''.format(n_clicks)

    app.run_server(debug=True)

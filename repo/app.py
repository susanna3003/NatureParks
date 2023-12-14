'''
this program is meant to display a webpage with different nc nature parks for user to browse by region and select for an informational file

@quayles
'''
from flask import Flask, render_template, request
import pandas

all_df = []

# creating df
state_df = pandas.read_csv('state_parks.csv', usecols=["Park Name", "Region", "County or Counties", "Status", "Remarks"])
all_df.append(state_df)
rec_df = pandas.read_csv('rec_parks.csv', usecols=["State Recreation Area", "Region", "Counties", "Status", "Remarks"])
all_df.append(rec_df)
nat_df = pandas.read_csv('nat_parks.csv', usecols=["State Natural Area", "Region", "Counties", "Public Access", "Remarks"])
all_df.append(nat_df)
lakes_df = pandas.read_csv('lakes.csv', usecols=["State Lake", "Adjoining State Park", "Counties", "Remarks"])
all_df.append(lakes_df)
rivers_df = pandas.read_csv('rivers.csv', usecols=["State River", "Region", "Remarks"])
all_df.append(rivers_df)
trails_df = pandas.read_csv('trails.csv', usecols=["State Trail", "Region", "Remarks"])
all_df.append(trails_df)

app = Flask(__name__)

# route for home page
@app.route("/")
def index():
    '''
    this is what happens in the home page
    '''
    return render_template("index.html")

# route for state parks page
@app.route("/state_parks", methods=["GET", "POST"])
def state_parks():
    '''
    this is the state parks page where they can search by region
    '''
    global region
    global filtered_df
    global selected_parks
    if request.method == "POST" :
        if request.form['action'] == "Get Parks":
            region = request.form['region']
    
            filtered_df = state_df[state_df['Region'] == region]

            state_names = list(filtered_df['Park Name'])
        
            return render_template("state_parks.html", parks= state_names, parks_df="", title="")
        
        elif request.form['action'] == "Select Parks":
            # display list of parks BEFORE selection made, so bottom section empty
            selected_parks = request.form.getlist("parks")
            filtered_selected = filtered_df[filtered_df['Park Name'].isin(selected_parks)]
            table_html = filtered_selected.to_html(index=False)
            write_to_csv(filtered_selected)
            return render_template("state_parks.html", parks=selected_parks, parks_df=table_html, title = "Your Parks")
            
    else:
        # display list of parks BEFORE selection made, so bottom section empty
        return render_template("state_parks.html", parks="",parks_df= "",title = "")

def write_to_csv(filtered_df):
    # Write DataFrame rows to a CSV file
        filtered_df.to_csv('state_parks_info.csv', index=False)

# route for rec areas page
@app.route("/rec_areas", methods=["GET", "POST"])
def rec_areas():
    '''
    this is the state parks page where they can search by region
    '''
    global region
    global filtered_recs_df
    global selected_recs
    if request.method == "POST" :
        if request.form['action'] == "Get Rec Areas":
            region = request.form['region']
    
            filtered_recs_df = rec_df[rec_df['Region'] == region]

            rec_names = list(filtered_recs_df['State Recreation Area'])
        
            return render_template("rec_areas.html", recs= rec_names, recs_df="", title="")
        
        elif request.form['action'] == "Select Rec Areas":
            # display list of parks BEFORE selection made, so bottom section empty
            selected_recs = request.form.getlist("recs")
            filtered_selected_recs = filtered_recs_df[filtered_recs_df['State Recreation Area'].isin(selected_recs)]
            recs_html = filtered_selected_recs.to_html(index=False)
            write_to_csv(filtered_selected_recs)
            return render_template("rec_areas.html", recs=selected_recs, recs_df=recs_html, title = "Your Recreation Areas")
            
    else:
        # display list of parks BEFORE selection made, so bottom section empty
        return render_template("rec_areas.html", recs="",recs_df= "",title = "")

def write_to_csv(filtered_df):
    # Write DataFrame rows to a CSV file
        filtered_df.to_csv('selected_recs_info.csv', index=False)

#route for nat areas page
@app.route("/nat_areas", methods=["GET", "POST"])
def nat_areas():
    '''
    this is the state parks page where they can search by region
    '''
    global region
    global filtered_nats_df
    global selected_nats
    if request.method == "POST" :
        if request.form['action'] == "Get Natural Areas":
            region = request.form['region']
    
            filtered_nats_df = nat_df[nat_df['Region'] == region]

            nat_names = list(filtered_nats_df['State Natural Area'])
        
            return render_template("nat_areas.html", nats= nat_names, nats_df="", title="")
        
        elif request.form['action'] == "Select Natural Areas":
            # display list of parks BEFORE selection made, so bottom section empty
            selected_nats = request.form.getlist("nats")
            filtered_selected_nats = filtered_nats_df[filtered_nats_df['State Natural Area'].isin(selected_nats)]
            nats_html = filtered_selected_nats.to_html(index=False)
            write_to_csv(filtered_selected_nats)
            return render_template("nat_areas.html", nats=selected_nats, nats_df=nats_html, title = "Your Natural Areas")
            
    else:
        # display list of parks BEFORE selection made, so bottom section empty
        return render_template("nat_areas.html", nats="",nats_df= "",title = "")

def write_to_csv(filtered_df):
    # Write DataFrame rows to a CSV file
        filtered_df.to_csv('selected_nats_info.csv', index=False)

@app.route("/lakes")
def lakes():
    '''
    this is what happens in the home page
    '''
    return render_template("lakes.html")

if __name__ == "__main__":
    app.run(debug=True)
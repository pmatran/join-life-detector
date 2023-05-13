
'''
	ZARA ITEMS CLASSIFIER MODEL APPLICATION
'''

# -- Import module
import os
import pandas as pd
from pycaret.classification import load_experiment, load_model, create_app

# -- Set addtional app components
title = "<h1 align=center style='font-size: 50px'>Join-Life Detector<h1>"

description = """
<p align=left style='font-size: 1.5em;'>
	Try the <i>Javier</i>&nbsp;favorite <strong style='color: #addbd0;'>
	Binary Classifier</strong>to find if your spanish Zara garment include 
	the special <i style='color: #addbd0;'>join-life</i> eco-label.
</p>
"""

# -- Read data
df = pd.read_parquet(os.path.join('data', 'ml', 'zara_items.parquet'))

# -- Load experiment
exp = load_experiment(
	path_or_file=os.path.join('store', 'Binary_classification_experiment'),
	data=df,
	preprocess_data=False
	)

# -- Load MLA best model
model = load_model(os.path.join('store', 'models', 'Voting_Classifier_Model'))

# -- Create join-life Prediction application
app_kwargs = {
	'title': title,
	'description': description,
	'theme':'Monochrome'
}
create_app(model, app_kwargs=app_kwargs)

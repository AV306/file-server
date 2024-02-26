from flask import *;

app = Flask( __name__ );

@app.route( "/<path:name>" )
def getFileAtPath( name ):
  print( f"File at {name} requested" );
  return send_from_directory( "./", name ); 

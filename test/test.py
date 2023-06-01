from streetviewext import sv_among_route
from dotenv import load_dotenv
import os

load_dotenv()

dir_api = os.environ.get('DIR_API')
view_api = os.getenv('VIEW_API')

print(dir_api)

sv_among_route(
    origin = "Section 2, Xinglong Rd, Wenshan District, Taipei City, 116", 
    destination="No. 115, Section 3, Xinglong Rd, Wenshan District, Taipei City, 116",
    mode="bicycling",
    dir_key=dir_api, 
    street_key=view_api, 
    save_destination="data",
    save_start_num=2,
)
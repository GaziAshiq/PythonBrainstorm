import requests

url = ''
res = requests.get('https://res.cloudinary.com/practicaldev/image/fetch/s--S7eEuRM5--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vjazrkhbg7ymabc8zsfo.png')

with open('graph.png', 'wb', encoding=res.encoding) as f:
    f.write(res.content)
import json, sys, os
import requests
from pyecharts import options as opts
from pyecharts.charts import Map

def ChinaMap():
    currentpath = os.path.dirname(sys.argv[0])
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53'}
    url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare'
    response = requests.get(url, headers)
    #print(response)
    #data = json.loads(response.json()['data']['provinceCompare'])
    data = response.json()['data']['provinceCompare']
    #print(data)

    '''
    # 1. list to render map
    provinces = []
    confirmed = []
    for k,v in data.items():
        provinces.append(k)
        confirmed.append(v['nowConfirm'])
    #print('provinces:', provinces)
    #print('confirmed:', confirmed)
    lst = [list(z) for z in zip(provinces, confirmed)]
    print(lst)
    '''
    # 2. dict to render map
    '''
    provinces = []
    for k,v in data.items():
        provinces.append([k, v['nowConfirm']])
    print('provinces:', provinces)
    '''
    provinces = [[k, v['nowConfirm']] for k, v in data.items()]
    print('provinces:', provinces)

    c=(
        Map().add(
            '',
            #[list(z) for z in zip(provinces, confirmed)],
            provinces,
            'china'
        ).set_series_opts(
            label_opts=opts.LabelOpts(is_show=True)
        ).set_global_opts(title_opts=opts.TitleOpts(title='国内疫情分布图'), visualmap_opts=opts.VisualMapOpts(max_=3000, is_piecewise=False)
        ).render(os.path.join(currentpath,'疫情图.html'))
    )

def main():
    ChinaMap()

    print('Done!')

if __name__ == '__main__':
    main()
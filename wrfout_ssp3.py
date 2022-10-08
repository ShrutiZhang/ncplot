#nc datasub and plot
    import netCDF4 as nc
    import pandas as pd
    import numpy as np
    file = r'D:\machine\data\meic\SSP1-26-BHE\grid\SSP1-26-BHE\2050\2050_00_total_VOC.nc'
    dataset =nc.Dataset(file)
    all_vars=dataset.variables.keys()
    print(all_vars)
    all_vars_info =list(dataset.variables.items())
    print(all_vars_info)
    #%%
    voc = dataset.variables['z'][:]
    lon = dataset.variables['x_range'][:]
    lat = dataset.variables['y_range'][:]
    time = dataset.variables['time']
    realtime = nc.num2date(time, time.units)
#%%plot with grid and map
    import matplotlib.pyplot as plt
    import matplotlib.colors as colors
    data=o3
    data2=data[i]
    plotname=str(realtime[i].year)+str('%02d'%(realtime[i].month))
    from mpl_toolkits.basemap import Basemap
    lon=dataset.variables['lon'][:]
    lat=dataset.variables['lat'][:]
    lon0 = lon.mean()
    lat0 = lat.mean()
    m=Basemap(llcrnrlon=60,
            llcrnrlat=10,
            urcrnrlon=150,
            urcrnrlat=60,
            projection='cyl', lat_0 = 50,lon_0=150)
    m.drawcoastlines()    # 海岸线
    m.drawcountries(linewidth=1)    # 国界线
# CHN_adm1的数据是中国各省区域
    m.readshapefile(shapefile='D:/machine/map/gadm36_CHN_shp/gadm36_CHN_1',
                name='states',
                drawbounds=True)
    m.drawparallels(np.arange(10., 70., 10.), labels=[1, 0, 0, 0], fontsize=10)
    m.drawmeridians(np.arange(60., 150., 10.), labels=[0, 0, 0, 1], fontsize=10)
    m.drawcoastlines() #plot coast line
    lon, lat = np.meshgrid(lon, lat)  #生成网格数据meshgrid是生成网格的函数，其中lons和lats是输入的横纵坐标
    xi, yi = m(lon, lat)  #绘制底图的坐标矩阵
    boundaries = np.arange(0, 0.5, 0.005)
    cmap_reds = plt.cm.get_cmap('jet_r', len(boundaries))
    cs = m.pcolormesh(xi, yi, data2, cmap='jet',
                      vmin=0, vmax=110
                      )  #pcolor函数是指使用xi和yi为横纵坐标，z值取np.squeeze(eva)，是颜色映射函数
    cbar = m.colorbar(location='bottom', pad="10%")
    font1 = {'family': 'DejaVu Sans', 'weight': 'normal', 'size': 16}
    plt.title(plotname, font1)
    plt.show()


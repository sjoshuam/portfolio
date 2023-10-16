##########==========##########==========##########==========##########==========

## import libraries
from os import listdir
from os.path import isdir
from shutil import copy

## define color scheme (with default for missing)
color_scheme = {
    'crowded_scatterplot': ('#FFFFFF', '#000000'),
    'pop_cluster_map': ('#FFF9F2', '#663D14'),
    'travel_suggestions': ('#000000', '#CCCCCC'),
    'travel_weather': ('#FFFFFF', '#000000'),
    'us_travels': ('#F2F9FF', '#143D66'),
    'better_state_borders': ('#FFFFFF', '#000000'),
    'life_expectancy': ('#000000', '#CCCCCC'),
    }

## import html template
with open('p/template.html', 'rt') as conn:
    template = conn.read()
    conn.close()
template = template.replace('{', 'Xyz').replace('}', 'xyZ')
template = template.replace('Abc', '{').replace('abC', '}')

## detect all deployable projects
all_projects = listdir('..')
deployable_projects = dict()
for i in all_projects:
    if isdir('../' + i + '/C_Output'):
        deployable_projects[i] = '../' + i + '/C_Output/' + i + '.png'
    if isdir('../' + i + '/C_Outputs'):
        deployable_projects[i] = '../' + i + '/C_Outputs/' + i + '.png'

print('CHANGE THIS FOR HTML PROJECTS')
for i in all_projects:
    if isdir('../' + i + '/out'):
        deployable_projects[i] = '../' + i + '/out/' + i + '.png'
    if isdir('../' + i + '/out'):
        deployable_projects[i] = '../' + i + '/out/' + i + '.png'
        
## deploy a project page for each eligible project
for i in deployable_projects.keys():
    
    ## lookup color specs
    if i in color_scheme.keys():
        bg_color = color_scheme[i][0]
        fg_color = color_scheme[i][1]
    else:
        bg_color = '#FFFFFF'
        fg_color = '#000000'
    
    
    ## generate html page
    with open('p/' + i + '.html', 'wt') as conn:
        html_page = template.format(bg_color, fg_color, i)
        html_page = html_page.replace('Xyz', '{').replace('xyZ', '}')
        conn.write(html_page)
        
    ## copy over poster
    copy(deployable_projects[i], 'p/' + i + '.png')
    
print('Done')
from django.shortcuts import redirect
import time
import docker
import os
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from dockerapi.forms import CreateForm, loginForm, CreateNetworkForm

def serviceupdate(request,servicename):
    if request.method == "GET":
        return render(request, 'update.html')
    elif request.method == "POST":

        client = docker.from_env() # docker api client 불러오기

        image_name = request.POST.get('imagename') # 받아올 update할 이미지 이름
        service_name = servicename # 업데이트할 서비스 이름(웹에서 선택)
    
        service = client.services.get(service_name) # service 객체 받아오기
        service.update(image=image_name) # 업데이트

        return redirect('/servicelist')
def servicerollback(request,servicename):
    service_name = servicename # 웹에서 받아올 rollback 할 서비스 이름
    command = 'docker service rollback ' + service_name # 롤백 명령어 작성

    ret = subprocess.run(command, shell=True, check=True) # 롤백 명령어 실행

    return redirect('/servicelist')

def servicescale(request,servicename):
    if request.method == "GET":
        return render(request, 'scaleout.html')
    elif request.method == "POST":
        client = docker.from_env()
        count = request.POST.get('count')
        service_name = servicename  # 웹에서 전달 받을 service name
        service = client.services.get(service_name)
        scale_num = int(count)   # 웹에서 전달 받을 scale 변경할 수
        service.scale(scale_num)

        return redirect('/servicelist')

def service_list(request):
    service_comm = 'docker service ls'
    service_stream = os.popen(service_comm)

   # 명령어 실행 결과 받아오기
    service_stream_output = service_stream.read()

   # TODO 문자열 파싱은 각자

   # 출력용 결과
    servicelist = service_stream_output.split()
    result=""
    for i in servicelist:
        result += i + "="
    #return HttpResponse(result)
    infos = []
    for i in range(6,len(servicelist),5):
        temp=[]
        for j in range(5):
            if len(servicelist) - i < 5:
                break
            temp.append(servicelist[i+j])
        infos.append(temp)
        
    context = {
            'infos':infos,
            }

    return render(request, 'netlisttables.html',context)
    

def main(request):
    stack_comm = 'docker stack ls'
    stack_stream = os.popen(stack_comm)
    stack_stream_output = stack_stream.read()    
    stacklist = stack_stream_output.split()

    infos = []
    for i in range(3,len(stacklist),3):
        temp = []
        temp.append(stacklist[i])
        temp.append(stacklist[i+1])
        temp.append(stacklist[i+2])
        infos.append(temp)

    context = {
            'infos':infos,
            }

    return render(request, 'tables.html',context)

def rmstack(request,stackname):
    stack_name =  stackname   
    rmstack_ins_comm = 'docker stack rm ' + stack_name
    stack_stream = os.popen(rmstack_ins_comm)
    stack_stream_output = stack_stream.read()
    return redirect('/main')

def psstack(request,stackname):
    stack_name =  stackname
    rmstack_ins_comm = 'docker stack ps ' + stack_name
    stack_stream = os.popen(rmstack_ins_comm)
    stack_stream_output = stack_stream.read()
    pslist = stack_stream_output.split()
    for i in range(len(pslist)):
        if i>= len(pslist):
            break
        if '\\' in pslist[i]:
            pslist.pop(i)
            
    infos = []
    for i in range(10,len(pslist),9):
        temp=[]
        
        if len(pslist)-i <9:
            break
        for j in range(5):
            temp.append(pslist[i+j])
        tmpstr = pslist[i+5]+' '+pslist[i+6]+' '+pslist[i+7] +' '+ pslist[i+8]
        temp.append(tmpstr)
        infos.append(temp)
        
    context = {
            'infos':infos,
            }

    return render(request, 'stackpstables.html',context)

def makevolume(request):
    if request.method == "GET":
        return render(request, 'volumemake.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":
        volumename = request.POST.get('volumename')

        mkvol_ins_comm = 'docker volume create ' + volumename
        vol_stream = os.popen(mkvol_ins_comm)
        vol_stream_output = vol_stream.read()
        return redirect('/volumelist')

def listvolume(request):
    net_comm = 'docker volume ls'
    net_stream = os.popen(net_comm)
    net_stream_output = net_stream.read()
    netlist = net_stream_output.split()
    netlist[1] += netlist[2]
    netlist.pop(2)

    infos = []
    for i in range(2,len(netlist),2):
        temp=[]
        temp.append(netlist[i])
        temp.append(netlist[i+1])

        infos.append(temp)

    context = {
            'infos':infos,
            }

    return render(request, 'volumelstables.html',context)
def volume_inspect(request,volumename):
    vol_name =  volumename   # 바꿔줘야해요
    vol_ins_comm = 'docker volume inspect ' + vol_name
    vol_stream = os.popen(vol_ins_comm)
    vol_stream_output = vol_stream.read()
    result = "<pre>"
    result += vol_stream_output
    result += "</pre>"
    return HttpResponse(result)
     

def volume_delete(request,volumename):
    vol_name =  volumename
    rmvol_ins_comm = 'docker volume rm ' + vol_name
    vol_stream = os.popen(rmvol_ins_comm)
    vol_stream_output = vol_stream.read()
    return redirect('/volumelist')

def network_list(request):
    net_comm = 'docker network ls'
    net_stream = os.popen(net_comm)
    net_stream_output = net_stream.read()
    netlist = net_stream_output.split()
    netlist[0] += netlist[1]
    netlist.pop(1)

    infos = []
    for i in range(4,len(netlist),4):
        temp=[]
        temp.append(netlist[i])
        temp.append(netlist[i+1])
        temp.append(netlist[i+2])
        temp.append(netlist[i+3])
        
        infos.append(temp)

    context = {
            'infos':infos,
            }

    return render(request, 'servicelstables.html',context)
def network_delete(request,networkname):

    net_name =  networkname 
    rmnetwork_ins_comm = 'docker network rm ' + net_name
    net_stream = os.popen(rmnetwork_ins_comm)
    net_stream_output = net_stream.read()
    return redirect('/networklist')
def network_inspect(request,networkname):
    net_name =  networkname   # 바꿔줘야해요
    net_ins_comm = 'docker network inspect ' + net_name
    net_stream = os.popen(net_ins_comm)
    net_stream_output = net_stream.read()
    result = "<pre>"
    result += net_stream_output
    result += "</pre>"
    list = result.split()
    string = ""
    for i in range(len(list)):
        string += list[i] + "<br>" 
    return HttpResponse(result)

def makeNetwork(request):
    if request.method == "GET":

        return render(request, 'createNetwork.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":
        createNetworkForm = CreateNetworkForm(request.POST)
        driver = request.POST.get('driver')
        name = request.POST.get('networkname')
        deploy_data_path = os.getcwd() + '/dockerapi/deploy_data'

        network_driver = driver
        network_name = name
        sh_path = deploy_data_path + '/shell/createNetwork.sh' # shell 파일 경로
        command = sh_path + ' ' + network_driver + ' ' + network_name # 실행할 명령어

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)
        return redirect('/networklist')


def login_docker(request):
    if request.method == "GET":

        return render(request, 'login2.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":

        deploy_data_path = os.getcwd() + '/dockerapi/deploy_data'
        docker_id = request.POST.get('dockerID') # 받아올 stack/service name
        docker_pw = request.POST.get('dockerTocken')
        sh_path = deploy_data_path + '/shell/login.sh' # shell 파일 경로
        command = sh_path + ' ' + docker_id + ' ' + docker_pw # 실행할 명령어

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)

        return redirect('/main')
def logout_docker(request):
        deploy_data_path = os.getcwd() + '/dockerapi/deploy_data'

        sh_path = deploy_data_path + '/shell/logout.sh' # shell 파일 경로
        command = sh_path # 실행할 명령어

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)

        return redirect('/')
def image_push(request):
    if request.method == "GET":

        return render(request, 'pushimage.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":

        imagename = request.POST.get('imagename') # 받아올 stack/service name
        tagname = request.POST.get('tagname')

        tag_ins_comm = 'docker tag ' + imagename +' localhost:5000/' +tagname
        tag_stream = os.popen(tag_ins_comm)
        tag_stream_output = tag_stream.read()

        push_comm = 'docker push localhost:5000/'+tagname
        push_stream = os.popen(push_comm)
        push_stream_output = push_stream.read()
        
        return redirect('/imagelist')
def image_pull(request):
    if request.method == "GET":
        return render(request, 'pullimage.html')
    elif request.method == "POST":
        imageurl = request.POST.get('imageurl')
        imagename = request.POST.get('imagename')
        mkimg_ins_comm="" 
        if imageurl == "":    
            mkimg_ins_comm = 'docker image pull ' + imagename
        else:
            mkimg_ins_comm = 'docker pull ' + imageurl+'/'+imagename
        img_stream = os.popen(mkimg_ins_comm)
        img_stream_output = img_stream.read()
        return redirect('/imagelist')
         # yml 파일 경로
def image_remove(request,imagename,imagetag):
    imagename = imagename.replace('~','/')
    net_comm = 'docker rmi ' + imagename + ':'+imagetag
    print(net_comm)
    net_stream = os.popen(net_comm)
    net_stream_output = net_stream.read()
    return redirect('/imagelist')
def image_list(request):
    net_comm = 'docker image ls'
    net_stream = os.popen(net_comm)
    net_stream_output = net_stream.read()
    netlist = net_stream_output.split()
    netlist[2] += netlist[3]
    netlist.pop(3)

    infos = []
    for i in range(5,len(netlist),7):
        temp=[]
        netlist[i] = netlist[i].replace('/','~')
        temp.append(netlist[i])
        temp.append(netlist[i+1])
        temp.append(netlist[i+2])
        if netlist[i+3] == "About":
            netlist.pop(i+4)
        tempstr = netlist[i+3] +' '+  netlist[i+4] + ' '+ netlist[i+5]
        temp.append(tempstr)
        temp.append(netlist[i+6])

        infos.append(temp)

    context = {
            'infos':infos,
            }

    return render(request, 'imagelisttables.html',context)

def create_image(request):
    if request.method == "GET":
        return render(request, 'imagemake.html')
    elif request.method == "POST":
        imagename = request.POST.get('imagename')
        yml = request.POST.get('imageyaml')
        deploy_data_path = os.getcwd()
        with open('/home/rapa/django/simpleDocker/Dockerfile', 'w') as f:
            f.write(yml)
        img_name =  imagename
        mkimg_ins_comm = 'docker build -t ' + img_name +' .'
        img_stream = os.popen(mkimg_ins_comm)
        img_stream_output = img_stream.read()

        time.sleep(2)
        return redirect('/imagelist')
         # yml 파일 경로

def create(request):
    # form page 띄우기
    if request.method == "GET":

        return render(request, 'stackmake.html')

    # form으로 입력받은 데이터 저장 밑 배포
    elif request.method == "POST":
        name = request.POST.get('stackname')
        yml = request.POST.get('stackyaml')
        deploy_data_path = os.getcwd() + '/dockerapi/deploy_data'
        with open('/home/rapa/django/simpleDocker/dockerapi/deploy_data/yml/temp.yml', 'w') as f:
            f.write(yml)

        yml_path = deploy_data_path + '/yml/temp.yml' # yml 파일 경로
        stack_name = name # 받아올 stack/service name
        sh_path = deploy_data_path + '/shell/deploy.sh' # shell 파일 경로
        command = sh_path + ' ' + yml_path + ' ' + stack_name # 실행할 명령어

        # subprocess 모듈을 통한 명령어 실행(외부파일실행)
        ret = subprocess.run(command, shell=True, check=True)
        time.sleep(3)
        return redirect('/main')

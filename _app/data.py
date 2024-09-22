from pathlib import Path
import base64
import sys

# Determine base paths dynamically depending on whether the app is frozen
if getattr(sys, 'frozen', False):  # If the script is bundled as an executable
    base_path = Path(sys._MEIPASS) / '_app/static/images'
else:
    base_path = Path('_app/static/images')

# Define the folders using the base path
projects_images = base_path / 'projects'
system_tools_images = base_path / 'system_tools'


class SystemTool:
    def __init__(self, name, links, image, doc, servers, dersciption="") -> None:
        self.name = name
        self.links = links
        self.image = self.image_to_base64(image)
        self.doc = doc
        self.servers = servers
        self.description = dersciption

    # Function to convert image to base64
    @staticmethod
    def image_to_base64(image_path):
        if image_path != '':
            with open(image_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode()
                return f"data:image/png;base64,{image_data}"


class QAProject:
    def __init__(self, name, links, image, doc, servers, dersciption="") -> None:
        self.name = name
        self.links = links
        self.image = self.image_to_base64(image)
        self.doc = doc
        self.servers = servers
        self.description = dersciption

    # Function to convert image to base64
    @staticmethod
    def image_to_base64(image_path):
        if image_path != '':
            with open(image_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode()
                return f"data:image/png;base64,{image_data}"


project_scheduler = QAProject(
    name="Project Scheduler",
    links=["http://testshell-03:5056/auth/login"],
    image=f"{projects_images}/project_scheduler.png",
    doc="",
    servers=["testshell-03"]
)

tv_dashboard = QAProject(
    name="TV Dashboard",
    links=["http://testshell-03:5065/", "http://testshell-04:5065/"],
    image=f"{projects_images}/tv.png",
    doc="",
    servers=["testshell-03", "testshell-04"]
)

kpi_dashboard = QAProject(
    name="KPI Dashboard",
    links=["http://testshell-03:5053/", "http://testshell-04:5053/"],
    image=f"{projects_images}/kpi.png",
    doc="",
    servers=["testshell-03", "testshell-04"])

monitor_dashboard = QAProject(
    name="Monitor Dashboard",
    links=["http://172.17.163.40:3001/dashboard"],
    image=f"{projects_images}/uptime_kuma.png",
    doc="",
    servers=[])

training_center = QAProject(
    name="Training Center",
    links=["http://testshell-03:5057/auth/login"],
    image=f"{projects_images}/training_center.png",
    doc="",
    servers=["testshell-03"])

performance_dashboard = QAProject(
    name="Performance Dashboard",
    links=["http://testshell-03:5055/auth/login"],
    image=f"{projects_images}/performance_dashboard.png",
    doc="",
    servers=["testshell-03"])


management_tool = QAProject(
    name="Management Tool",
    links=["http://testshell-03:5050/auth/login"],
    image=f"{projects_images}/management_tool.png",
    doc="",
    servers=["testshell-03"])

rad_logo = QAProject.image_to_base64(f'{projects_images}/rad_logo.png')

apps = [project_scheduler, tv_dashboard,
        kpi_dashboard, monitor_dashboard,
        training_center, performance_dashboard,
        management_tool]


bitbucket = SystemTool(
    name="BitBucket",
    links=["http://bitbucket1:7990/login"],
    image=f"{system_tools_images}/bitbucket.jpg",
    doc="",
    servers=[]
)

jira = SystemTool(
    name="Jira",
    links=["https://radc.atlassian.net/jira/your-work"],
    image=f"{system_tools_images}/jira.png",
    doc="",
    servers=[]
)

jenkins = SystemTool(
    name="Jenkins",
    links=["http://rnd1-shabtai-3.ad.rad.co.il:8080/"],
    image=f"{system_tools_images}/jenkins.png",
    doc="",
    servers=[]
)

system_tools = [bitbucket, jira, jenkins]

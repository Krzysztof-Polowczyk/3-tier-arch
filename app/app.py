from flask import Flask, request, Response
from flask.typing import ResponseValue

from app.controlers import controlers
from app.repositoris import persitance


App = Flask(__name__)


@App.get("/users/<int:id>")
def get_via_id(id:int, repo=persitance(
    {
            1:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            3:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        })) -> ResponseValue:
    controller = controlers(repo)
    try:
        out = controller.get(id)
        return out, 200
    except ValueError:
        return {}, 404


@App.get("/users")
def get_all(repo=persitance(
    {
            1:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            3:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        })) -> ResponseValue:
    
    controller = controlers(repo)

    out = controller.get_all()
    if out: return out, 200
    return {}, 404


@App.post("/users")
def add(repo=persitance(
    {
            1:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            3:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        })
    ,inner_request = request) -> ResponseValue:
    
    controller = controlers(repo)
    try:
        controller.put(inner_request.json)
        return Response(status=200)
    except ZeroDivisionError:
        return Response(status=422)

    


@App.patch("/users/<int:id>")
def patch_endpoint(id:int ,repo=persitance(
    {
            1:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            3:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        })
    ,inner_request = request) -> ResponseValue:
    
    controller = controlers(repo)
    try:
        controller.patch(id ,inner_request.json)
        return Response(status=200)
    except ZeroDivisionError:
        return Response(status=422)
    except ValueError:
        Response(status=404)




@App.delete("/users/<int:id>")
def delete_endpoint(id:int ,repo=persitance(
    {
            1:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            3:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        })
    ,inner_request = request) -> ResponseValue:
    
    controller = controlers(repo)
    try:
        controller.dellete(id)
        return Response(status=200)
    except ValueError:
        return Response(status=404)



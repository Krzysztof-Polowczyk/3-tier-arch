from flask import Flask, request, Response
from flask.typing import ResponseValue

from app.controlers import controlers
from app.repositoris import persitance


App = Flask(__name__)


@App.get("/users/<int:id>")
def get_via_id(id, repo=persitance(
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

    out = controller.get(id)
    if isinstance(out, ValueError): return {}, 422
    if out: return out, 200
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
    controller.put(inner_request)

    return Response(status=200)

@App.patch("/users/<int:id>")
def patch_endpoint(id ,repo=persitance(
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
    controller.patch(id ,inner_request.json)

    return Response(status=200)


@App.delete("/users/<int:id>")
def delete_endpoint(id ,repo=persitance(
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
    controller.dellete(id)

    return Response(status=200)


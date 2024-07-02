import yaml

REDIRECTS = {
    "/google": "google.com",
    "/bing": "bing.com",
    "/softwaresim": "softwaresim.com/pricing/"
}

specification = {
    "defaultService": "projects/YOUR_PROJECT/global/backendBuckets/YOUR_BACKEND_BUCKET_SERVICE",
    "name": "matcher",
    "routeRules": []
}

for i, uri in enumerate(REDIRECTS.keys()):
    specification["routeRules"].append({
        "urlRedirect": {
            "pathRedirect": "/" + "/".join(REDIRECTS[uri].split("/")[1:]),
            "stripQuery": True,
            "hostRedirect": REDIRECTS[uri].split("/")[0]
        },
        "matchRules": [
            {
                "prefixMatch": uri
            }
        ],
        "priority": i
    })

print(yaml.dump(specification))
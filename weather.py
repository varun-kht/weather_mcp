import httpx

async def get_weather(city:str):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    
    async with httpx.AsyncClient() as client:
        geo = await client.get(
            geo_url,
            params={"name":city,"count":1}

        )

        geo_data = geo.json()

        if "results" not in geo_data:
            return {"error":"city not found"}
        
        lat = geo_data["results"][0]["latitude"]
        lat = geo_data["results"][0]["longitude"]

        weather = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
            }

        )
        weather_data = weather.json()

        return {
            "city": city,
            "temperature": weather_data["current_weather"]["temperature"],
            "windspeed": weather_data["current_weather"]["windspeed"]
        }
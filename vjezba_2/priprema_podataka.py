import asyncio, random, time


async def proizvodi():
    print("Dohvačanje proizvoda")
    await asyncio.sleep(random.uniform(1, 3))
    print("Zavrsetak dohvacanja proizvoda")
    return [
        {"id": 1, "name": "Bežični miš", "price": 24.9, "category": "Periferija"},
        {"id": 2, "name": "USB-C hub", "price": 34.5, "category": "Dodaci"},
    ]

async def dostava():
    print("Dohvačanje dostave")
    await asyncio.sleep(random.uniform(1, 3))
    print("Zavrsetak dohvacanja dostave")
    return [
        {"id": 1, "name": "Preuzimanje u trgovini", "price": 0, "days": 1},
        {"id": 2, "name": "Standardna dostava", "price": 3.5, "days": 4},
        {"id": 3, "name": "Brza dostava", "price": 7.9, "days": 1},
    ]

async def recenzije():
    print("Dohvačanje recenzija")
    await asyncio.sleep(random.uniform(1, 3))
    print("Zavrsetak dohvacanja recenzija")
    return [
        {"id": 1, "customer": "Ana", "rating": 5, "comment": "Brza dostava i sve je stiglo uredno zapakirano."},
        {"id": 2, "customer": "Marko", "rating": 4, "comment": "Dobre cijene, ali izbor bi mogao biti veći."},
        {"id": 3, "customer": "Petra", "rating": 5, "comment": "Podrška mi je odmah pomogla oko zamjene proizvoda."},
        {"id": 4, "customer": "Ivan", "rating": 3, "comment": "Proizvod je u redu, no paket je kasnio dva dana."},
    ]



async def main():
    pocetak = time.perf_counter()

    task_proizvodi = asyncio.create_task(proizvodi())
    task_dostava = asyncio.create_task(dostava())
    task_recenzije = asyncio.create_task(recenzije())

    podaci_proizvodi = await task_proizvodi
    podaci_dostava = await task_dostava
    podaci_recenzije = await task_recenzije

    kraj = time.perf_counter()

    print(f"Ukupno vrijeme izvođenja: {kraj - pocetak:.2f} s")

asyncio.run(main())

import asyncio

async def saludar():
  print("Hola")
  await asyncio.sleep(2.5)
  print("Adios")


async def main():
  print("Iniciado el programa")

  while True:
    print("Im iterating")
    await asyncio.sleep(1)
    asyncio.create_task(saludar())

asyncio.run(main())
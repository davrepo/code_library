import time
import multiprocessing
import concurrent.futures
from PIL import Image, ImageFilter

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

def multiprocess_old():
    processes = []
    
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()


def multiprocess_new():     # returns the results in the order they were finished
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # results = [executor.submit(do_something, 1) for _ in range(10)]
        results = [executor.submit(do_something, sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

def multiprocess_map():     # returns the results in the order they were started
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for result in results:
            print(result)

def image_processing():
    img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg']
    
    size = (1200, 1200)
    # for img_name in img_names:
    #     img = Image.open(img_name)
    #     img = img.filter(ImageFilter.GaussianBlur(15))
    #     img.thumbnail(size)
    #     img.save(f'processed/{img_name}')
    #     print(f'{img_name} was processed...')
        
    def process_image(img_name):
        img = Image.open(img_name)
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size)
        img.save(f'processed/{img_name}')
        print(f'{img_name} was processed...')
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)
    

def main():
    # start = time.perf_counter()
    # multiprocess_old()
    # finish = time.perf_counter()
    # print(f'Finished in {round(finish-start, 2)} second(s)')
    
    # start = time.perf_counter()
    # multiprocess_new()
    # finish = time.perf_counter()
    # print(f'Finished in {round(finish-start, 2)} second(s)')
    
    # start = time.perf_counter()
    # multiprocess_map()
    # finish = time.perf_counter()
    # print(f'Finished in {round(finish-start, 2)} second(s)')

    start = time.perf_counter()
    image_processing()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
    
if __name__ == "__main__":
	main()
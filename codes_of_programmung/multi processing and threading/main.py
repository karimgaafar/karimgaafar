# # import  multiprocessing
# # import time
# # def calc_square(list):
# #     value_of_square=0
# #     for i in list:
# #         value_of_square+=i*i
# #         print(f"result of square is :{value_of_square}")
# #         time.sleep(1)
# #
# # def calc_cube(list):
# #     value_f_cube=0
# #     for i in list:
# #         value_f_cube=i*i*i
# #         print(f"result of cube is :{value_f_cube}")
# #         time.sleep(3)
# #
# # if __name__== "__main__":
# #     arr=[3,5,7]
# #     p1=multiprocessing.Process(target=calc_square,args=(arr,))
# #     p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
# #     p1.start()
# #     p2.start()
# #     p1.join()
# #     p2.join()
# #
# #
# # import os
# # import multiprocessing
# #
# #
# # #in multi processing each procsee has its own id
# # #but in threading all has one address
# #
# #
# # def function1():
# #     print("ID of process running func2: {}".format(os.getpid()))
# #
# # def function_2():
# #     print("ID of process running func 1: {}".format(os.getpid()))
# #
# #
# # if __name__== "__main__":
# #     print(f" id of main process is :{os.getpid()}")
# #     p1=multiprocessing.Process(target=function1)
# #     p2=multiprocessing.Process(target=function_2)
# #     p1.start()
# #     p2.start()
# #     p1.join()
# #     p2.join()
# # import multiprocessing
# # result=[]
# # #there is a proplem
# # def function1(list):
# #     global result
# #     for i in list:
# #         result.append(i*i)
# #     print(f"result of array is {result}")
# # if __name__=="__main__":
# #     list=[2,4,8]
# #     p1=multiprocessing.Process(target=function1,args=(list,))
# #     p1.start()
# #     p1.join()
# #     print(f" result in main process{result}")
# # to solve this process make 3 parameter(result,array)
# import multiprocessing
# def function_1(result,array):
#     for idx,num in enumerate(array):
#         result[idx]=num*num
#     print(f" the resilt in function1 {result[:]}")
#
# if __name__=="__main__":
#     elemnts=[3,5,7]
#     result=multiprocessing.Array('i',3)
#     p1=multiprocessing.Process(target=function_1,args=(result,elemnts,))
#     p1.start()
#     p1.join()
#     print(f"result in main processs{result[:]} ")
# import multiprocessing
# def  square_list(elements,queue):
#     for i in elements:
#         queue.put(i)
# def return_square_list(queue):
#     print("queue elements")
#     while  not queue.empty():
#         print(queue.get())
#     print(" queue elemnts is empty now")
# if __name__=="__main__":
#     elements=[3,5,7]
#     Q1=multiprocessing.Queue()
#     #make two process
#     p1=multiprocessing.Process(target=square_list,args=(elements,Q1,))
#     p2=multiprocessing.Process(target=return_square_list,args=(Q1,))
#
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
# import time
#
# def calc_square(numbers):
#     print("calculate square numbers \n")
#     for n in numbers:
#         print('square:',n*n , '\n')
#         time.sleep(0.2) #simulate an I/O-bound task
#
# def calc_cube(numbers):
#     print("calculate cube of numbers \n")
#     for n in numbers:
#         print('cube:',n*n*n , '\n')
#         time.sleep(0.2) #simulate an I/O-bound task
#
# arr = [2,3,8,9]
#
# t = time.time()
#
# calc_square(arr)
# calc_cube(arr)
#
#
# print("done in : ",time.time()-t)
# print("Hah... I am done with all my work now!")

# import time
# import threading
#
# def calc_square(numbers):
#     print("calculate square numbers \n")
#     for n in numbers:
#         print('square:',n*n , '\n')
#         time.sleep(0.2) #simulate an I/O-bound task
#
# def calc_cube(numbers):
#     print("calculate cube of numbers \n")
#     for n in numbers:
#         print('cube:',n*n*n , '\n')
#         time.sleep(0.2) #simulate an I/O-bound task
#
# arr = [2,3,8,9]
#
# t = time.time()
#
# t1= threading.Thread(target=calc_square, args=(arr,))
# t2= threading.Thread(target=calc_cube, args=(arr,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("done in : ",time.time()-t)
# print("Hah... I am done with all my work now!")

#create the thread_pool by concurrent.futures
# import concurrent.futures
#
#
# def worker():
#     print("Worker thread running")
#
# #max_worker is =1 mean that one work only execute in one time
# pool=concurrent.futures.ThreadPoolExecutor(max_workers=3)
#
# pool.submit(worker)
# pool.submit(worker)
#
#
# pool.shutdown(wait=True)

# print("Main thread continuing to run")
# import  time
# import concurrent.futures
# def square_result(list):
#     for i in list:
#         print(f"result of square {i*i}")
#         time.sleep(2)
# def cube_result(list):
#     for i in list:
#         print(f"result of cube is {i*i*i}")
#         time.sleep(2)
#
# arr=[2,4,8]
# pool=concurrent.futures.ThreadPoolExecutor(max_workers=2)
# pool.submit(square_result,arr)
# pool.submit(cube_result,arr)
# pool.shutdown(wait=True)
#race condution task
# import threading
# import time
# x=0
# def increment():
#     global x
#
#
#     x+=1
# def main_function(loc):
#     for i in range(100):
#         loc.acquire()
#         increment()
#         loc.release()
#     print(x)
# if __name__=="__main__":
#     lock=threading.Lock()
#     p1=threading.Thread(target=main_function,args=(lock,))
#     p2=threading.Thread(target=main_function,args=(lock,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
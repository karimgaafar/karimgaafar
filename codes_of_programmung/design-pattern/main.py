#facade
# class subsytema_a:
#     def opreation_a(self):
#         print(" this is opreation A")
# class subsystem_b:
#     def opreation_b(self):
#         print(" this  is opreation B ")
# class subsystem_c:
#     def opreation_c(self):
#         print("this opreation C")
# class make_all:
#     def __init__(self):
#         self.system_a=subsytema_a()
#         self.system_b=subsystem_b()
#         self.system_c=subsystem_c()
#     def function_all_opreation(self):
#         self.system_a.opreation_a()
#         self.system_b.opreation_b()
#         self.system_c.opreation_c()
# x=make_all()
# x.function_all_opreation()
#flyweight
# class flyweight:
#     shared_state={}
#     def __init__(self,name):
#         self.name=name
#         self.unique_state=None
#     def unique_state(self,unique_state):
#         self.unique_state=unique_state
#         print(f" flyweught {self.name} doing opreation with {self.unique_state}")
# class create_flyweiht:
#     flyweight_dic={}
#     def get_shared_state(self,shared_state):
#         self.shared_state=shared_state
#         if shared_state not in self.flyweight_dic:
#             self.flyweight_dic[shared_state]=flyweight(shared_state)
#             print(" shared state is done createed")
#         else:
#             print("shared state is exist")
# x=create_flyweiht()
# fly1=x.get_shared_state("ahmed")
# fly2=x.get_shared_state("karim")

#singelton
# class singelton:
#     #class method or static method this two function that can calling them from the class
#     #return refernce to it self and is ensures that only one instance of the class is ever created
#     def __new__(cls):
#         return cls
#     #make it static to can callit by class
#     @staticmethod
#     def return_name():
#         print("hello wolrd")
#     #make it classmethod to can call it by class
#     @classmethod
#     def return_age(cls):
#         print(" my age is :34")
# x=singelton()
# x2=singelton()
# x3=singelton()
# print(f"id of singelton {id(singelton)}")
# print(f"id of singelton {id(x2)}")
# print(f"id of singelton {id(x3)}")
#builder
# from abc import ABCMeta, abstractmethod
# class interface_builder(metaclass=ABCMeta):
#     def builder_part_a(self):
#         pass
#     def builder_part_b(self):
#         pass
#     def builder_part_c(self):
#         pass
#     def get_result(self):
#         pass
# class product():
#     def __init__(self):
#         self.parts=[]
#  #take  object from class name product that we append in it my create
# class create_builder(interface_builder):
#     def __init__(self):
#         self.product=product()
#     def builder_part_a(self):
#         self.product.parts.append("a")
#         # because when we call function each function refer to it self
#         return self
#     def builder_part_b(self):
#         self.product.parts.append("b")
#         # because when we call function each function refer to it self
#         return self
#     def builder_part_c(self):
#         self.product.parts.append("c")
#         # because when we call function each function refer to it self
#         return self
#     def get_result(self):
#         return self.product
# class director:
#     @staticmethod
#     def get_all():
#         return create_builder().builder_part_a().builder_part_b().builder_part_c().get_result()
# x=director().get_all()
# print(x.parts)



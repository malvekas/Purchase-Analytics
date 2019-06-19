
import sys

class order:
    def __init__(self):
        self.prod_dept={}
        self.dept_order={}
        self.dept_reorder={}
    
    def get_prod_dept(self,filename):
        with open(filename,mode="r") as f:
            next(f)
            for line in f:
                s=line.rstrip().split(',')
                if int(s[0]) not in self.prod_dept.keys():
                    self.prod_dept[int(s[0])]=int(s[-1])

    def order_count(self,filename):
        with open(filename,mode="r") as f:
            next(f)
            for line in f:
                s=line.rstrip().split(',')
                if int(s[1]) in self.prod_dept.keys():
                    self.dept_order[self.prod_dept[int(s[1])]]=self.dept_order.get(self.prod_dept[int(s[1])],0)+1
                    if int(s[3])==0:
                        self.dept_reorder[self.prod_dept[int(s[1])]]= self.dept_reorder.get(self.prod_dept[int(s[1])],0)+1
                    else:
                        self.dept_reorder[self.prod_dept[int(s[1])]]= self.dept_reorder.get(self.prod_dept[int(s[1])],0)+0
    
    def output_file(self,filename):
        with open(filename,mode="w") as f:
            f.write("department_id,number_of_orders,number_of_first_orders,percentage\n")
            for i in sorted(self.dept_order.keys()):
                f.write("%s,%s,%s,%s\n"%(i,self.dept_order[i],self.dept_reorder[i],format((self.dept_reorder[i]*1.0)/self.dept_order[i],'.2f')))
                

def main(argv):
    if len(sys.argv)<3:
        print("2 Input files are required: product and order_product. 1 output file required.")
        print("<scriptname> <inputfile1> <inputfile2> <outputfile>")
        sys.exit()
    else:
        filep=sys.argv[1]
        fileo=sys.argv[2]
        outfile=sys.argv[3]
    
    orderobj=order()
    orderobj.get_prod_dept(filep)
    orderobj.order_count(fileo)
    orderobj.output_file(outfile)
    
if __name__ == '__main__':
    main(sys.argv[1:])


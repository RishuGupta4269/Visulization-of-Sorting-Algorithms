import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def swap(A,i,j):
    a=A[j]
    A[j]=A[i]
    A[i]=a
    
def bubble(arr,l):
    for i in range(0,l-1):
        for j in range(0,l-i-1):
            if(arr[j]>arr[j+1]):
                swap(arr,j,j+1)
            yield arr
        
     
def selection(arr,l):
    for i in range(l-1):
        m=arr[i]
        pos=i
        for j in range(i+1,l):
            if(m>arr[j]):
                m=arr[j]
                pos=j
            yield arr    
        if(pos!=i):
            swap(arr,i,pos)
            yield arr

def quick_Sort(arr,p,q):
    if(p>=q):
        return
    piv = arr[q]
    pivindx = p
    for i in range(p,q):
        if(arr[i]<piv):
            swap(arr,i,pivindx)
            pivindx+=1
        yield arr
    swap(arr,q,pivindx)
    yield arr

    yield from quick_Sort(arr,p,pivindx-1)
    yield from quick_Sort(arr,pivindx+1,q)
 
def merge(arr,lb,mid,ub):
    b=[]
    i=lb
    j=mid+1
    while(i<=mid and j<=ub):
        if(arr[i]<=a[j]):
            b.append(arr[i])
            i+=1
        else:
            b.append(arr[j])
            j+=1
    
    if(i>mid):
        while(j<=ub):
            b.append(arr[j])
            j+=1
    
    else:
        while(i<=mid):
            b.append(arr[i])
            i+=1
    
    for i,val in enumerate(b):
        arr[i+lb]=val
        yield arr
    
def merge_Sort(arr,p,q):
    if(p>=q):
        return
    mid=int((p+q)/2)
    yield from merge_Sort(arr,p,mid)
    yield from merge_Sort(arr,mid+1,q)
    yield from merge(arr,p,mid,q)
    
    yield arr

def heapify(arr,i,l):
    lc=2*i+1
    rc=2*i+2
    m=i
    if(lc<l and arr[lc]>arr[m]):
        m=lc
    if(rc<l and arr[rc]>arr[m]):
        m=rc
    if(m!=i):
        swap(arr,m,i)
        yield arr
        yield from heapify(arr,m,l)

def heap_Sort(arr,l):
    for i in range(int (l/2),-1,-1):
        yield from heapify(arr,i,l)
        
    for i in range(l-1,0,-1):
        swap(arr,0,i)
        yield arr
        yield from heapify(arr,0,i)
        
def insertion_Sort(arr,l):
    for i in range(1,l):
        t=arr[i]
        j=i-1
        while(j>=0 and arr[j]>t):
            arr[j+1]=arr[j]
            j-=1
            yield arr
        arr[j+1]=t
        yield arr

def shell_Sort(arr,l):
    g=int(l/2)
    while(g>=1):
        for j in range(g,l):
            i=j-g
            while(i>=0):
                if(arr[i+g]>arr[i]):
                    break;
                else:
                    swap(arr,i+g,i)
                    yield arr
                i=i-g
            yield arr
        g=int(g/2)

def count_Sort(arr,exp,n,count,d):
    op=[0]*(n)
    
    
    for i in range(0,n):
        ind=int(arr[i]/exp)
        count[int(ind%d)]+=1
    
    for i in range(1,10):
        count[i]+=count[i-1]
    
    i=n-1
    while i>=0:
        ind=int(arr[i]/exp)
        op[count[(ind)%d]-1]=arr[i]
        count[(ind)%d]-=1
        i-=1
    
    for i in range(0,n):
        arr[i]=op[i]
        yield arr

            

    
def radix_Sort(arr,n):
    max1=n
    e=1
    while int(max1/e)>0:
        coun=[0]*(10)
        yield from count_Sort(arr,e,n,coun,10)
        e*=10
        yield arr
        
        
n=int(input("Enter the number of elements:"))
ch=input("Menu: \n1. Bubble Sort \n2. Selection Sort \n3.Merge Sort\n4.Quick Sort\n5.Heap Sort\n6.Insertion Sort\n7.Shell Sort\n8.Radix Sort\nEnter exit to quit\n" )
a=[x for x in range(1,n+1)]
random.shuffle(a)
if(ch=='1'):
    algo=bubble(a,n)
    title="Bubble Sort"
elif(ch=='2'):
    algo=selection(a,n)
    title="Selection Sort"
elif(ch=='3'):
    algo=merge_Sort(a,0,n-1)
    title="Merge Sort"
elif(ch=='4'):
    algo=quick_Sort(a,0,n-1)
    title="Quick Sort"
elif(ch=='5'):
    algo=heap_Sort(a,n)
    title="Heap Sort"
elif(ch=='6'):
    algo=insertion_Sort(a,n)
    title="Insertion Sort"
elif(ch=='7'):
    algo=shell_Sort(a,n)
    title="Shell Sort"
elif(ch=='8'):
    algo=radix_Sort(a,n)
    title="Radix Sort"
    
    #elif(ch.lower()=="exit"):
        #break

fig,ax=plt.subplots()
ax.set_title(title)

bar_rec=ax.bar(range(n),a,align='edge')

ax.set_xlim(0,n+1)
ax.set_ylim(0,n+1)
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

epochs = [0]



def update_plot(array, rec, epochs):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))
    

def on_press(event):
    if event.key.isspace():
        if anima.running:
            anima.event_source.stop()
        else:
           anima.event_source.start()
        anima.running ^= True
         
fig.canvas.mpl_connect('key_press_event', on_press)

anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
anima.running = True
anima.direction = +1
plt.show()

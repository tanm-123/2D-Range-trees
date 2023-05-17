def merge(l1,l2):
    i=0
    j=0
    l=[]
    while i<len(l1) and j<len(l2):
        if l1[i][1] < l2[j][1]:
            l.append(l1[i])
            i = i + 1
        else:
            l.append(l2[j])
            j = j + 1
    while i < len(l1):
        l.append(l1[i])
        i = i + 1
    while j < len(l2):
        l.append(l2[j])
        j = j + 1
    return(l)
class Node:
    def __init__(self,val,left,right,ylist):
        self.val=val
        self.left=left
        self.right=right
        self.ylist=ylist
class BST:  
    def __init__(self):
        self.pythonroot=None
    def buildtree(self,list):
            n=len(list)
            if n==0:
                    return None
            if n==1:
                    node=Node(list[0],None,None,list)
            else:
                m=n//2
                node=Node(list[m],self.buildtree(list[:m]),self.buildtree(list[m+1:]),None)
                if node.left!=None:
                    l1=node.left.ylist
                if node.right!=None:
                    l2=node.right.ylist
                if node.left!=None and node.right!=None:
                    l4=merge(l1,l2)
                    l5=[node.val]
                    node.ylist=merge(l4,l5)
                if node.left!=None and node.right==None:
                    l3=[node.val]
                    node.ylist=merge(l1,l3)
                if node.left==None and node.right!=None:
                    l6=[node.val]
                    node.ylist=merge(l2,l6)
            return node
class PointDatabase:
    def __init__(self,pointlist):
        self.pointlist=pointlist
        pointlist.sort()
        bst=BST()
        n=bst.buildtree(pointlist)
        self.root=n
    def searchNearby(self, q, d):
        ans=[]
        x=q[0]
        y=q[1]
        xmin=x-d
        xmax=x+d
        ymin=y-d
        ymax=y+d
        if self.root==None:
            return ans
        if xmin<self.root.val[0]<xmax:
            l=self.root
        else:
            l=self.root
            while l.val[0]<xmin or l.val[0]>xmax:
                if l.val[0]<xmin:
                    if l.right==None:
                        return ans
                    l=l.right
                if l.val[0]>xmax:
                    if l.left==None:
                        return ans
                    l=l.left
        t=l.val
        if ymin<=t[1]<=ymax:
            ans.append(t)
        if l.left==None and l.right==None:
            return ans    
        else:
            if l.left!=None:
                m=l.left
                t=m.val
                if xmin<=t[0]<=xmax:
                    if ymin<=t[1]<=ymax:
                        ans.append(t)
                while (m.left!=None or m.right!=None):
                    if xmin<=(m.val)[0]:
                        if m.right==None:
                            m=m.left
                            if m==None:
                                break
                            t=m.val
                            if xmin<=t[0]<=xmax:
                                if ymin<=t[1]<=ymax:
                                    ans.append(t)
                        else:
                            s=m.right
                            w=s.ylist
                            n=len(w)
                            if n==1:
                                if ymin<=w[0][1]<=ymax:
                                    ans.append(w[0])
                            else:
                                if (ymax>=w[0][1] and ymin<=w[n-1][1]):
                                    g=0
                                    h=n-1
                                    ys=n-1
                                    while g<=h:
                                        mid = g + (h-g+1)//2
                                        if w[mid][1]>ymin:
                                            ys=mid
                                            h=mid-1
                                        elif w[mid][1]<ymin:
                                            g=mid+1
                                        elif w[mid][1]==ymin:
                                            ys=mid
                                            break
                                    yp=0
                                    low=0
                                    high=n-1
                                    while low<=high:
                                        mid = low +(high-low+1)//2
                                        if w[mid][1]<ymax:
                                            yp=mid
                                            low=mid+1
                                        elif w[mid][1]>ymax:
                                            high=mid-1
                                        elif w[mid][1]==ymax:
                                            yp=mid
                                            break
                                    for i in range(ys,yp+1):
                                        ans.append(w[i])
                            m=m.left
                            if m==None:
                                break
                            t=m.val
                            if xmin<=t[0]<=xmax:
                                if ymin<=t[1]<=ymax:
                                    ans.append(t)
                    else:
                        m=m.right
                        if m==None:
                            break
                        t=m.val
                        if xmin<=t[0]<=xmax:
                            if ymin<=t[1]<=ymax:
                                ans.append(t)
            if l.right!=None:
                k=l.right
                t=k.val
                if xmin<=t[0]<=xmax:
                    if ymin<=t[1]<=ymax:
                        ans.append(t)
                while (k.left!=None or k.right!=None):
                    if xmax>=(k.val)[0]:
                        if k.left==None:
                            k=k.right
                            if k==None:
                                break
                            t=k.val
                            if xmin<=t[0]<=xmax:
                                if ymin<=t[1]<=ymax:
                                    ans.append(t)
                        else:
                            s=k.left
                            w=s.ylist
                            n=len(w)
                            if n==1:
                                if ymin<=w[0][1]<=ymax:
                                    ans.append(w[0])
                            else:
                                if (ymax>=w[0][1] and ymin<=w[n-1][1]):
                                    g=0
                                    h=n-1
                                    ys=n-1
                                    while g<=h:
                                        mid = g + (h-g+1)//2
                                        if w[mid][1]>ymin:
                                            ys=mid
                                            h=mid-1
                                        elif w[mid][1]<ymin:
                                            g=mid+1
                                        elif w[mid][1]==ymin:
                                            ys=mid
                                            break
                                    yp=0
                                    low=0
                                    high=n-1
                                    while low<=high:
                                        mid = low +(high-low+1)//2
                                        if w[mid][1]<ymax:
                                            yp=mid
                                            low=mid+1
                                        elif w[mid][1]>ymax:
                                            high=mid-1
                                        elif w[mid][1]==ymax:
                                            yp=mid
                                            break
                                    for i in range(ys,yp+1):
                                        ans.append(w[i])
                            k=k.right
                            if k==None:
                                break
                            t=k.val
                            if xmin<=t[0]<=xmax:
                                if ymin<=t[1]<=ymax:
                                    ans.append(t)
                    else:
                        k=k.left
                        if k==None:
                            break
                        t=k.val
                        if xmin<=t[0]<=xmax:
                            if ymin<=t[1]<=ymax:
                                ans.append(t)
        return ans
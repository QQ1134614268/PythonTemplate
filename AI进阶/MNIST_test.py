from sklearn.datasets import fetch_mldata

minst=fetch_mldata("MNIST Original",data_home="MNIST_data" )
print(minst.data.shape)

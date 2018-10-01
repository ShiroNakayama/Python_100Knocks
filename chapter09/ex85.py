# 85. 主成分分析による次元圧縮
# 84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
from scipy import io
from sklearn.decomposition import TruncatedSVD

# 単語文脈行列を読み込む
X = io.loadmat("word_context_matrix")["X"]

# 次元を圧縮して結果を出力する
pca = TruncatedSVD(n_components=300)
X_300 = pca.fit_transform(X)
io.savemat("word_context_matrix_dim300", {"X_300": X_300})

# 確認のため次元を表示
print(f"original: {X.shape}")
print(f"after PCA: {X_300.shape}")

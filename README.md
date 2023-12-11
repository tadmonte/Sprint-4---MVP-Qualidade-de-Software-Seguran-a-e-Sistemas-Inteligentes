# Meu Front

Este pequeno projeto faz parte do MVP da Disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes ** 


---
## Como executar Front

Basta fazer o download do projeto e abrir o arquivo index.html no seu browser.
---

## Como executar Back

Executar o comando: python -m flask run --host 0.0.0.0 --port 5000
---

## **Conclusão do Modelo**

O notebook utiliza-se de uma base de dados onde recebemos 4 informações relevantes: Receita Total, Limite, Target e Pedidos Feitos, onde analisados busca-se saber se o cliente é potencial ou não.

Para definição do modelo, quatro modelos base (KNN, Decision Tree, Naive Bayes, SVM) foram comparados usando validação cruzada estratificada.

A análise incluiu avaliações em três configurações de dados: original, padronizado e normalizado, onde foi possível perceber que o KNN original obteve o melhor resultado.

Como o KNN com métrica euclidiana e apenas 1 vizinho obteve os melhores resultados, a otimização de hiperparâmetros não foi necessária.

A avaliação final do modelo no conjunto de teste atendeu ao critério de 75% para a métrica Recall.

A simulação em novos dados mostrou a capacidade do modelo otimizado em lidar com entradas não vistas.

Por fim, o pipeline proporciona uma base sólida para futuras iterações e refinamentos do modelo. A inclusão de padronização, normalização e otimização de hiperparâmetros contribui para um desempenho robusto. A análise crítica dos resultados é essencial, destacando a importância de métricas apropriadas e uma compreensão profunda do problema em questão.

 ## **LINKS**

Link Video: https://www.youtube.com/watch?v=riqYWd0UblY
OBS: Realizei alterações a fim de melhorar no meu modelo depois de gravar o video, a parte da aplicação está igual. O collab esta atualizado.

Link DataSet: https://raw.githubusercontent.com/tadmonte/Sprint-4---MVP-Qualidade-de-Software-Seguran-a-e-Sistemas-Inteligentes/main/api/database/DataClientesNew.csv

Link MODELO MVP 4: https://colab.research.google.com/drive/1pspe0D3HvhZc-oaKSdXV9Pl249x8x6TP?usp=sharing

Link Classificação dos Modelos com POO e Sem POO:  https://colab.research.google.com/drive/1a1YSwqdIX4larkQS0ErEPLOusbB-aCE5?usp=sharing

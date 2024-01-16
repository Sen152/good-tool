3 对于CIFAR10、mnnist等 dataloader构造好以后 ，方便查看nonidd数据
data_loader = DataLoader(dataset, batch_size=batch_size)
        target_counts = {}
        for data, target in data_loader:
            for t in target:
                target_counts[t.item()] = target_counts.get(t.item(), 0) + 1

        # 打印类别数量
        allsample=0
        for target, count in target_counts.items():
            print(f"class {target} is{count}",end=' ;')
            allsample+=count
        print(f"共计 {allsample}")

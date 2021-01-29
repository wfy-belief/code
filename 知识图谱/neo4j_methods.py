from typing import Dict, List, Any, NoReturn

from py2neo import Graph, Node, Relationship, NodeMatcher


class MyNeo4j(object):
    """docstring for My_neo4j of 2020.1.1 version
       Created by wfy-belief
       Any bug or problem email wfy-belief@foxmail.com
       Contact me for extra function by QQ 1335680234
       Maybe it is helpful https://cloud.tencent.com/developer/article/1434904
    """
    __slots__ = '__graph'

    def __init__(self,
                 scheme: str = 'bolt',
                 host: str = 'localhost',
                 user: str = 'neo4j',
                 password: str = 'wfy'):
        """
        Args:
            scheme: 协议类型 默认 bolt(速度快-稳定) 可选 http
            host: 主机IP 默认 localhost
            user: 用户名 默认 neo4j
            password: 密码 默认 wfy
        """
        try:
            # 连接neo4j数据库，输入协议，地址、用户名、密码
            self.__graph = Graph(scheme=scheme,
                                 host=host,
                                 user=user,
                                 password=password
                                 )
        except Exception as e:
            print(e)
        else:
            print('连接成功', self.__graph)
        finally:
            print(self.__graph.call.dbms.components())

    def delete_all(self) -> NoReturn:
        """
        Returns:
            None 清除neo4j中原有的结点等所有信息
        """
        self.__graph.delete_all()
        print('清除neo4j中原有的结点等所有信息成功')
        return None

    def add_relationship(self,
                         source: Dict[Any, Any],
                         relationship: str,
                         target: Dict[Any, Any],
                         source_labels: List[str] = ('paper',),
                         target_labels: List[str] = ('person',),
                         *,
                         build_new_nodes: List[bool] = (False, False)) -> NoReturn:
        """
        description:
            构造两个节点 和 关系的名字 生成关系
        Args:
            *:
            build_new_nodes: 控制source target 是否新建节点 默认为False
            source: 类型 dict 传递一个字典,必须包含 'name' 其它键不限制
            relationship: 类型 str 传递一个字符串 表示关系
            target:类型 dict 传递一个字典,必须包含 'name' 其它键不限制
            source_labels (List):List 元素字符串 列表元组都可以 表示source标签 可以是多标签
            target_labels (List):List 元素字符串 列表元组都可以 表示target标签 可以是多标签

        Returns:
            None
        """
        build_new_source_node, build_new_target_node = build_new_nodes
        # 转换为Node类型
        source = self.__dict_to_node(source_labels, source, new_node=build_new_source_node)
        target = self.__dict_to_node(target_labels, target, new_node=build_new_target_node)
        # 创建关系
        relation = Relationship(source, relationship, target)
        self.__graph.create(relation)
        return None

    def __dict_to_node(self,
                       labels: List[str],
                       dict_data: Dict[Any, Any],
                       *, new_node: bool = False) -> Node:
        """
        description:
            把数据转换为Node节点类型
        Args:
            *:
            new_node: 是否构建新节点，默认False
            labels: Tuple[str]节点的标签
            dict_data: Dict[str] = str 节点的树形 name 键必须含有

        Returns:
            1.如果节点存在返回原节点
            2.如果节点不存在新建一个节点
            3.标签可以少查询多 不能多标签查询少标签数据
            4.支持特殊情况，直接调用新节点，不查找
        """
        if new_node:
            return Node(*labels, **dict_data)
        matcher = NodeMatcher(self.__graph)
        # 如果结点存在直接返回
        node = matcher.match(*labels, **dict_data).first()
        if node:
            return node
        return Node(*labels, **dict_data)
